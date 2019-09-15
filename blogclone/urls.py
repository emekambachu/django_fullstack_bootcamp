from django.urls import path
from . import views

# Template Tagging
app_name = 'blogclone'

urlpatterns = [

    # class based views
    path('',
         views.PostListView.as_view(),
         name='list-posts'),

    path('about',
         views.AboutView.as_view(),
         name='about'),

    path('<int:pk>/',
         views.PostDetailView.as_view(),
         name='post_detail'),

    path('post/create',
         views.CreatePostView.as_view(),
         name='create-post'),

    path('post/<int:pk>/edit',
         views.PostUpdateView.as_view(),
         name='edit-post'),

    path('post/<int:pk>/delete',
         views.PostDeleteView.as_view(),
         name='delete-post'),

    path('post/drafts',
         views.DraftListView.as_view(),
         name='post-drafts'),

    path('post/<int:pk>/comment',
         views.add_comment_to_post,
         name='add-comment-to-post'),

    path('comment/<int:pk>/approve',
         views.comment_approve,
         name='approve-comment'),

    path('comment/<int:pk>/remove',
         views.comment_remove,
         name='remove-comment'),

    path('post/<int:pk>/publish',
         views.post_publish,
         name='publish-post'),

]