from django.http import HttpResponse
from django.template import loader
from .models import *
from django.conf import settings
from django.shortcuts import redirect
from utils import dataLayerPDF
from utils import dprint
import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def homePage(request):
    
    template = loader.get_template('base_intro.html')
    context = {
       
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
	print(user.id)
	if user is not None:
		login(request, user)
		return redirect('systemForms')
		
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


@login_required
def viewSystemForms(request):
	pdfforms=PDFForm.objects.all()
	context = {
		'systemforms':pdfforms ,
	}
	template = loader.get_template('formsList.html')
	return HttpResponse(template.render(context, request))

@login_required
def addFormToProfile(request,form_id):
	#return HttpResponse(str(form_id))
	errorCondition=False
	loggedUserID=request.user.id
	UserObject=request.user
	PDFormObject=PDFForm.objects.get(id=form_id)
	#print(len(PDFormObject))
		
	isFormPresent=GeneratedPDF.objects.filter(user=UserObject, pdf=PDFormObject).count()
	if(isFormPresent==0):
		addform=GeneratedPDF(user=UserObject, pdf=PDFormObject)
		addform.save()


	return HttpResponse("Form Added to Profile")
		

    


def logoutUser(request):
	logout(request)
	return redirect('login')

def fillForm(request):
	

	userID=1
	pdfid=1

	#get details about the form
	formData=PDFForm.objects.get(id=pdfid)
	#get all fields in PDF related to PDFID
	fieldsinPDF=PDFFormField.objects.filter(pdf=pdfid).values_list(
																	"field",
																	"field_x",
																	"field_page_number",
																	"field_y",
																	"field_x_increment",
																	"field_choice",
																	"font_size",
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
	#print(userFields)
	userFieldDF=pd.DataFrame(list(userFields)).set_index('field')
	PDFFieldsDF=pd.DataFrame(list(fieldsinPDF)).set_index('field')
	
	#Make the Join
	combinedDF=userFieldDF.join(PDFFieldsDF, on='field',lsuffix='_left', rsuffix='_right')
	#remove rows with NA Values. Will happen when the number of rows in the above datasets differ in count. 
	combinedDF.dropna(0,inplace=True)
	
	#sort the Dataframe by Field Page Number, then convert it to a list of dictionaries
	dataSet=combinedDF.sort_values(by=['field_page_number']).to_dict('records')
	

	#print(dataSet)
	#Use the dataset as input to generate the pdf, recieve a buffer as reponse 
	pdfData=dataLayerPDF.addText(dataSet,formData)
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
