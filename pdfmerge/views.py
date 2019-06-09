from django.http import HttpResponse
from django.template import loader


def getUsers(request):
    users = User.objects.all()
    template = loader.get_template('index.html')
    context = {
        'userList': users,
    }
    return HttpResponse(template.render(context, request))