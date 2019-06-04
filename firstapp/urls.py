from django.urls import path
from . import views

# Template Tagging
app_name = 'firstapp'

urlpatterns = [
    
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('users', views.users, name='add-users'),

]