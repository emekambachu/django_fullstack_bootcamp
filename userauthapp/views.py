from django.shortcuts import render
from . forms import *

# imports for authentication views
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'userauthapp/index.html')

@login_required # use this if login is required for view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userauthapp:home'))

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('userauthapp:home'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password {}".format(username, password))
            return HttpResponse("Invalid Login Details Supplied")
    else:
        return render(request, 'userauthapp/login.html', {})



def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # hash password
            user.set_password(user.password)

            # save
            user.save()


            profile = profile_form.save(commit=False)

            # from the onetoone relationship
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'userauthapp/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

