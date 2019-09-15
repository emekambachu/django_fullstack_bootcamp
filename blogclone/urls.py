from django.urls import path
from . import views

# Template Tagging
app_name = 'blogclone'

urlpatterns = [

    # class based view
    path('/', views.PostListView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create', views.CreatePostView.as_view(), name='create-post'),

]