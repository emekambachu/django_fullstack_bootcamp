from django.urls import path
from . import views

# Template Tagging
app_name = 'userauthapp'

urlpatterns = [
    
    path('', views.index, name='home'),
	path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),

]