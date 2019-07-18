from django.http import HttpResponse
from django.template import loader
from . models import *
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

@login_required
@require_http_methods(["POST"])
def saveEditedField(request):
	fieldID=request.POST["fieldID"]
	fieldValue=request.POST["fieldValue"]
	formID=request.POST['formID']
	user=request.user

	if(not formID.isdigit()):
		return HttpResponse(status=500)

	if(not fieldID.isdigit()):
		return HttpResponse(status=500)

	# see first if user has the form associated with their profile

	userFormRelation=GeneratedPDF.objects.filter(user=user, pdf=formID).count()


	if(userFormRelation==0):
		return HttpResponse(status=500)



	 # User has the form added in their profile


	fieldData=[]
	fieldDict={}
	fieldDict["ID"]=fieldID
	fieldDict["userValue"]=fieldValue
	fieldData.append(fieldDict)

	modelUtils.saveUserProfileFields(fieldData, request.user)

	return HttpResponse("OK")

@login_required
@require_http_methods(["POST"])
def saveFormFieldSequence(request):
	superUser=request.user.is_superuser
	
	if(not superUser):
		return HttpResponse(status=404)


	fieldIDs=request.POST["fieldData"]	
	formID=request.POST['formID']
	user=request.user

	if(not formID.isdigit()):
		return HttpResponse(status=500)

	fieldIDList=fieldIDs.split(",")
	index=0
	for fieldID in fieldIDList:
		PDFFormField.objects.filter(pdf=formID, field=int(fieldID)).update(field_index=index)
		index=index+1

	#print(fieldIDList)

	return HttpResponse("OK")

