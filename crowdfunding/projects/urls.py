from django.urls import path #This imports the path function from Django’s urls module. The path function is used to define URL patterns that map URLs to views.
from . import views #This imports the views.py file from the current directory. views typically contains the logic for what happens when a specific URL is accessed (in this case, the logic for handling requests related to projects).

urlpatterns = [
  path('projects/', views.ProjectList.as_view()), #This line maps the URL 'projects/' to the ProjectList view.
  #views.ProjectList.as_view() is used to convert the ProjectList class (which inherits from APIView) into a view function that Django can use to handle HTTP requests.
  path('pledges/', views.PledgeList.as_view()),
  path('projects/<int:pk>/', views.ProjectDetail.as_view())
]