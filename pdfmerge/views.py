from django.http import HttpResponse
from django.template import loader
from .models import *
from django.conf import settings
from django.shortcuts import redirect
from utils import dataLayerPDF
from utils import dprint
import pandas as pd

def getUsers(request):
    users = CustomUser.objects.all()
    template = loader.get_template('index.html')
    context = {
        'userList': users,
    }
    return HttpResponse(template.render(context, request))
	
def loginForm(request):
	context = {
        'errors': "",
    }
	template = loader.get_template('registration/login.html')
	return HttpResponse(template.render(context, request))
	
	
def loginUser(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def fillForm(request):
	

	userID=1
	pdfid=1

	

	#get all fields in PDF related to PDFID
	fieldsinPDF=PDFFormField.objects.filter(pdf=pdfid).values_list(
																	"field",
																	"field_x",
																	"field_page_number",
																	"field_y",
																	"field_x_increment",
																	 named=True 
																	 )
	
	#get all fields Related to User in UserProfile and that match the fields in the PDFForm
	userFields=UserProfile.objects.filter(user=userID).values_list(
																	"field", 
																	"field_text",
																	"field_date",																	
																	named=True
																	)
	#dprint.dprint(queryset)

	#Set the column as index on which the join is to be made in pandas
	userFieldDF=pd.DataFrame(list(userFields)).set_index('field')
	PDFFieldsDF=pd.DataFrame(list(fieldsinPDF)).set_index('field')
	
	#Make the Join
	combinedDF=userFieldDF.join(PDFFieldsDF, on='field',lsuffix='_left', rsuffix='_right')
	#remove rows with NA Values. Will happen when the number of rows in the above datasets differ in count. 
	combinedDF.dropna(0,inplace=True)
	
	#sort the Dataframe by Field Page Number, then convert it to a list of dictionaries
	dataSet=combinedDF.sort_values(by=['field_page_number']).to_dict('records')
	

	print(dataSet)
	#Use the dataset as input to generate the pdf, recieve a buffer as reponse 
	pdfData=dataLayerPDF.addText(dataSet)
	# #output=dataLayerPDF.mergePDFs()

	
	#Set the httpresponse to download a pdf
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="dataLayer.pdf"'
	#response.write(PDFBytes)

	#write the pdfdata to the responseobject
	pdfData.write(response)
	#print(userFieldDF)

	#return the response 
	return response
	
	#return fieldData
	#context = {'UserData': dataSet,}
	#template = loader.get_template('pdf.html')
	#return HttpResponse(template.render(context, request))
