from django.urls import path
from . import views

# Template Tagging
app_name = 'secondapp'

urlpatterns = [
    
    path('', views.index, name='home'),
	path('users', views.users, name='users'),

]