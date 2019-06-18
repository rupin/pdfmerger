from django.http import HttpResponse
from django.template import loader
from .models import *
from django.conf import settings
from django.shortcuts import redirect
from utils import dataLayerPDF
from utils import dprint

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

	querysetdata=PDFFormField.objects.all().select_related()

	dprint.dprint(querysetdata)

	# pdfData=dataLayerPDF.addText(fieldData)
	# #output=dataLayerPDF.mergePDFs()
	# response = HttpResponse(content_type='application/pdf')
	# response['Content-Disposition'] = 'attachment; filename="dataLayer.pdf"'
	# #response.write(PDFBytes)
	# pdfData.write(response)
	
	#return fieldData
	context = {'UserData': querysetdata,}
	template = loader.get_template('pdf.html')
	return HttpResponse(template.render(context, request))
