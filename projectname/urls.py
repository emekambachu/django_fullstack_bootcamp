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

urlpatterns = [
    path('admin/', admin.site.urls),

    # use this when you import views from a specific app
    path('', views.index, name='index'),

    # including the firstapp app to the root project
    path('firstapp/', include('firstapp.urls')),

    # including the firstapp app to the root project
    path('secondapp/', include('secondapp.urls')),

    # including the firstapp app to the root project
    path('userauthapp/', include('userauthapp.urls')),
]
