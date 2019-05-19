#import for render and redirection
from django.shortcuts import render, redirect

# Import http response to process http requests
from django.http import HttpResponse

# import forms from current directory
from . import forms

# Create your views here.

def index(request):
    my_dict = {
        'insert_me':"hello i am something !"
    }
    return render(request, 'index.html', context=my_dict)


def contact(request):

    #get form class from forms.py
    contact_form = forms.ContactForm()

    return render(request, 'contact.html', {'contact_form':contact_form})