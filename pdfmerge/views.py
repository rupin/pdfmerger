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
	# newField={}
	# fieldData=[] 
	# newField["x"]=137
	# newField["y"]=676
	# newField["text"]="Rupin Raghavji Chheda"
	# newField["h-inc"]=17
	# newField["page"]=0
	# newField["type"]="block-text"
	# fieldData.append(newField)

	# newField={}
	# newField["x"]=135
	# newField["y"]=494
	# newField["text"]="India"
	# newField["h-inc"]=17
	# newField["page"]=0
	# newField["type"]="block-text"
	# fieldData.append(newField)

	userID=1
	pdfid=1

	#queryset=PDFFormField.objects.raw('SELECT * FROM pdfmerge_pdffromfield WHERE pdf = %s', [pdfid])

	#get all fields in PDF related to PDFID
	fieldsinPDF=PDFFormField.objects.filter(pdf=pdfid).values_list(
																	"field",
																	"field_x",
																	"field_page_number",
																	"field_y",
																	"field_x_increment",
																	 named=True 
																	 )
	# fieldIDs=[]
	# for myfield in fieldsinPDF:
	# 	fieldIDs.append(myfield.field_id)
	# print(fieldIDs)
	#get all fields Related to User in UserProfile and that match the fields in the PDFForm
	userFields=UserProfile.objects.filter(user=userID).values_list(
																	"field", 
																	
																	"field__field_type"
																	,named=True
																	)
	#dprint.dprint(queryset)

	userFieldDF=pd.DataFrame(list(userFields)).set_index('field')
	PDFFieldsDF=pd.DataFrame(list(fieldsinPDF)).set_index('field')
	# pdfData=dataLayerPDF.addText(fieldData)
	# #output=dataLayerPDF.mergePDFs()
	# response = HttpResponse(content_type='application/pdf')
	# response['Content-Disposition'] = 'attachment; filename="dataLayer.pdf"'
	# #response.write(PDFBytes)
	# pdfData.write(response)
	#print(userFieldDF)
	combinedDF=userFieldDF.join(PDFFieldsDF, on='field',lsuffix='_left', rsuffix='_right')
	print(newDF)

	
	#return fieldData
	context = {'UserData': fieldsinPDF,}
	template = loader.get_template('pdf.html')
	return HttpResponse(template.render(context, request))
