from django.urls import path
from . import views

# Template Tagging
app_name = 'cbvapp'

urlpatterns = [
    
    # Function based view
    # path('', views.index, name='home'),

    # class based view
    path('', views.CBView.as_view()),
    path('indexview', views.IndexView.as_view()),
    path('schools', views.SchoolListView.as_view(), name='schools')
]