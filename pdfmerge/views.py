from django.http import HttpResponse
from django.template import loader
from .models import *
from django.conf import settings
from django.shortcuts import redirect

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
	