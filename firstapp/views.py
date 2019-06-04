# import for render and redirection
from django.shortcuts import render, redirect

# Import http response to process http requests
# from django.http import HttpResponse

# import forms.py from current directory
from . import forms

# import AddUserForm from modelforms.py in current directory
from . modelforms import AddUserForm

# import Users from secondapp/models
# from secondapp.models import Users

# Create your views here.

def index(request):
    my_dict = {
        'insert_me':"hello i am something !"
    }
    return render(request, 'firstapp/index.html', context=my_dict)


def contact(request):

    #get form class from forms.py
    contact_form = forms.ContactForm()

    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST)

        if contact_form.is_valid():
            print("Validated")
            contact_form.cleaned_data['name']


    return render(request, 'firstapp/contact.html', {'contact_form':contact_form})


def users(request):
    add_user_form = AddUserForm()

    if request.method == "POST":
        add_user_form = AddUserForm(request.POST)

        if add_user_form.is_valid():
            add_user_form.save(commit=True)
            return index(request)
        else:
            print('ERROR INVALID')

    return render(request, 'firstapp/users.html', {'add_user_form':add_user_form})