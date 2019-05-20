#import for render and redirection
from django.shortcuts import render, redirect

# Import http response to process http requests
from django.http import HttpResponse

from . models import User

def index(request):
    return render(request, 'secondapp/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'secondapp/users.html', context=user_dict)