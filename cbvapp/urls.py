from django.urls import path
from . import views

# Template Tagging
app_name = 'cbvapp'

urlpatterns = [
    
    path('', views.index, name='home'),

]