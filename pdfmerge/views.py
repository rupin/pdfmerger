from django.http import HttpResponse
from django.template import loader
from .models import *

def getUsers(request):
    users = CustomUser.objects.all()
    template = loader.get_template('index.html')
    context = {
        'userList': user_list,
    }
    return HttpResponse(template.render(context, request))