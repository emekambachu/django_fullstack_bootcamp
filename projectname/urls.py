"""projectname URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

# import path and includes for app inclusion and paths to work
from django.urls import path, include

# you can also import the views from the app and use it directly without using the 'include'
from firstapp import views

# import views from blog clone
from blogclone import views as bloclone_views

# import authentication views from python
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # use this when you import views from a specific app
    # path('', views.index, name='index'),

    # including the firstapp to the root project
    path('firstapp/', include('firstapp.urls')),

    # including the secondapp to the root project
    path('secondapp/', include('secondapp.urls')),

    # including the userauthapp to the root project
    path('userauthapp/', include('userauthapp.urls')),

    # including the cbvapp to the root project
    path('cbvapp/', include('cbvapp.urls')),

    # including the blogclone to the root project
    path('blogclone/', include('blogclone.urls')),

    # add login path for imported auth
    path('blogclone/accounts/login', views.LoginView.as_view(), name='login'),

    # add logout path for imported auth
    path('blogclone/accounts/logout', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),

    path('accounts/profile/', bloclone_views.ProfileView.as_view(), name='profile-page'),

]
