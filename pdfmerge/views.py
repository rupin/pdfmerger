from django.http import HttpResponse
from django.template import loader
from .models import *
from django.conf import settings
from django.shortcuts import redirect
from utils import dataLayerPDF
from utils import dprint
from utils import modelUtils

import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.dateparse import parse_date 

import datetime
from dateutil.parser import *

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
	#print(user)
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
	
		
	isFormPresent=GeneratedPDF.objects.filter(user=UserObject, pdf=PDFormObject).count()
	if(isFormPresent==0):
		addform=GeneratedPDF(user=UserObject, pdf=PDFormObject)
		addform.save()
	


	
	#get all fields in PDF related to PDFID
	fieldsinPDF=PDFFormField.objects.filter(pdf=form_id).values_list(
																	"field",																
																	"field__field_display",
																	"field__field_question",
																	"field__field_state",																	
																	 named=True
																	 )
	
	#get all fields Related to User in UserProfile and that match the fields in the PDFForm
	userFields=UserProfile.objects.filter(user=loggedUserID).values_list(
																	"field", 
																	"field_text",																																		
																	named=True
																	)
	#print(userFields)
	#print(fieldsinPDF)

	#Set the column as index on which the join is to be made in pandas
	
	userFieldDF=pd.DataFrame(list(userFields)).set_index('field')
	PDFFieldsDF=pd.DataFrame(list(fieldsinPDF)).set_index('field')

	#dprint.dprint(userFieldDF)

	#dprint.dprint(PDFFieldsDF)
	
	#Make the Join
	combinedDF=PDFFieldsDF.join(userFieldDF, on='field',lsuffix='_left', rsuffix='_right')
	#remove rows with NA Values. Will happen when the number of rows in the above datasets differ in count. 
	#combinedDF.dropna(0,inplace=True)
	
	#sort the Dataframe by Field Page Number, then convert it to a list of dictionaries
	#dataSet=combinedDF.sort_values(by=['field_page_number']).to_dict('records')


	#dprint.dprint(combinedDF)
	
	missingQuestionsList=combinedDF[combinedDF["field__field_state"]=='DYNAMIC']
	missingQuestionsList.fillna(value='',inplace=True)
	missingQuestionsList.reset_index(inplace=True)
	#missingQuestionsList['field_str']=missingQuestionsList['field'].astype(str)
	

	missingQuestionTuples=list(missingQuestionsList.itertuples())
	#print(type(missingQuestionTuples))
	fieldIDStr=""
	for question in missingQuestionTuples:
		fieldIDStr=fieldIDStr+" " +str(question.field)
	fieldIDStr=fieldIDStr.strip().replace(" ", ",")
	#print(fieldIDStr)
	numberOfMissingQuestions=len(missingQuestionTuples)
	context = {
		'formObject':PDFormObject,
		"missingQuestions":missingQuestionTuples,
		'questionCount':numberOfMissingQuestions,
		'form_id':form_id,
		'fieldIDS':fieldIDStr
	}
	#dprint.dprint(missingQuestionsList)
	print(context)
	template = loader.get_template('process_form.html')
	return HttpResponse(template.render(context, request))
		

@login_required
@require_http_methods(["POST"])
def saveDynamicFieldData(request,pdfid):
	
	recievedDateFormat=""
	fieldIDs=request.POST["fieldIDs"]
	fieldIDList=[]
	fieldData=[]
	
	if(fieldIDs is not None):
		fieldIDList=fieldIDs.split(",")

	for fieldID in fieldIDList:
		fieldDict={}
		fieldDict["ID"]=fieldID
		fieldDict["userValue"]=request.POST[fieldID]
		fieldData.append(fieldDict)

	print(fieldData)
	modelUtils.saveUserProfileFields(fieldData, request.user)	


	
	return redirect('/viewPDF/'+str(pdfid))

    


def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required
def fillForm(request, pdfid):

	loggedUserID=request.user.id
	#pdfid=pdf_id

	#get details about the form
	formData=PDFForm.objects.get(id=pdfid)
	
	#get all fields in PDF related to PDFID
	fieldsinPDF=PDFFormField.objects.filter(pdf=pdfid).values_list(
																	"field",
																	"field_x",
																	"field_page_number",
																	"field_y",
																	"field_x_increment",
																	"field__field_display",
																	"font_size",
																	 named=True 
																	 )
	
	#get all fields Related to User in UserProfile and that match the fields in the PDFForm
	userFields=UserProfile.objects.filter(user=loggedUserID).values_list(
																	"field", 
																	"field_text",																																	
																	named=True
																	)
	#dprint.dprint(queryset)

	#Set the column as index on which the join is to be made in pandas
	#print(userFields)
	userFieldDF=pd.DataFrame(list(userFields)).set_index('field')
	PDFFieldsDF=pd.DataFrame(list(fieldsinPDF)).set_index('field')
	
	#Make the Join
	combinedDF=userFieldDF.join(PDFFieldsDF, on='field',lsuffix='_left', rsuffix='_right')
	combinedDF.sort_values(by=['field_page_number'],inplace=True)
	#
	#remove rows with NA Values. Will happen when the number of rows in the above datasets differ in count. 
	combinedDF.dropna(0,inplace=True)
	#dprint.dprint(combinedDF)
	#sort the Dataframe by Field Page Number, then convert it to a list of dictionaries
	dataSet=combinedDF.to_dict('records')
	

	#print(dataSet)
	#Use the dataset as input to generate the pdf, recieve a buffer as reponse 
	pdfData=dataLayerPDF.addText(dataSet,formData)
	# #output=dataLayerPDF.mergePDFs()

	
	#Set the httpresponse to download a pdf
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; filename="dataLayer.pdf"'
	#response.write(PDFBytes)

	#write the pdfdata to the responseobject
	pdfData.write(response)
	#response.write(pdfData)

	#return the response 
	return response
	
	

@login_required
def profile(request):
	template = loader.get_template('base_view_profile.html')
	context = {
		
	}
	return HttpResponse(template.render(context, request))	
