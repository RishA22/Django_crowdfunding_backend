"""
URL configuration for crowdfunding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin #This imports Django's admin site, which is used to manage the models and data in the application through a web interface.
from django.urls import path, include #This imports the path function, which is used to define URL patterns, The include function allows you to include other URL configuration files from different apps within your Django project. This helps in organizing URLs across multiple apps.
from users.views import CustomAuthToken


urlpatterns = [ #This defines the main URL configuration list for the entire project. It's where you map URLs to views or other URL configurations.
    path('admin/', admin.site.urls), #This maps the URL /admin/ to the Django admin site. When users visit this URL, they can access the admin interface.
    path('', include('projects.urls')), #This includes the URL configurations from the projects app. The include('projects.urls') function loads the URL patterns defined in projects/urls.py and incorporates them into the main project’s URL configuration.
    #The empty string '' as the URL pattern means that this will be the root URL, so any URLs defined in projects.urls will be available from the root (e.g., /projects/).
    path('', include('users.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(),name='api_token_auth'),    
]
