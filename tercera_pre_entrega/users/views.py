from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
    all_users = User.objects.all().values()

    template = loader.get_template('list_users.html')
    
    context = {
        'my_users': all_users,
    }
    print(request)
    return HttpResponse(template.render(context))

def details(request, id):
    user = User.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'user': user
    }
    return HttpResponse(template.render(context, request))
    