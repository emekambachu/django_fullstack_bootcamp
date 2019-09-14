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
    path('schools', views.SchoolListView.as_view(), name='schools'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create-school', views.SchoolCreateView.as_view(), name='create-school'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
]