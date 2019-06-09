from django.http import HttpResponse
from django.template import loader


def getUsers(request):
    user_list = CustomUser.objects()
    template = loader.get_template('index.html')
    context = {
        'userList': user_list,
    }
    return HttpResponse(template.render(context, request))