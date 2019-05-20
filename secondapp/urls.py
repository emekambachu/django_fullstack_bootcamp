from django.urls import path
from secondapp import views

urlpatterns = [
    
    path('', views.index, name='home'),
	path('users', views.users, name='users'),

]