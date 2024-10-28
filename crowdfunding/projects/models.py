from django.db import models
from django.contrib.auth import get_user_model #to import Django's get_user_model function, which allows you to access the current user model in your project, In Django, you can replace the default User model with a custom one (for example, CustomUser). If you do this, get_user_model() is a safe way to reference the user model because it dynamically retrieves the model you specified in AUTH_USER_MODEL in settings.py. This makes your code flexible and avoids hardcoding the user model name.

# Create your models here.
class Project(models.Model):
  project_name = models.CharField(max_length=200) # A short text field for the project title
  description = models.TextField() # A longer text field for the project description
  goal = models.IntegerField() # An integer field to store a project goal, e.g., a funding goal
  image = models.URLField() # A URL field to store the link to an image
  is_open = models.BooleanField() # A boolean field to check if the project is open or closed
  create_date = models.DateTimeField(auto_now_add=True) # Stores the date and time when the project was created
  end_date = models.DateTimeField()
  owner = models.ForeignKey(
       get_user_model(),
       on_delete=models.CASCADE,
       related_name='owned_projects'
   )


class Pledge(models.Model): #This defines a new Django model called Pledge. It inherits from models.Model, which means it is a database table.
  amount = models.IntegerField() #This field stores the amount of money pledged by the user as an integer (e.g., 100 dollars).
  comment = models.CharField(max_length=200) #This field stores an comment provided by the user when making the pledge.
  anonymous = models.BooleanField() #This field stores a Boolean value (True or False), which indicates whether the user wants to remain anonymous. If True, their name might be hidden when displaying the pledge publicly.
  project = models.ForeignKey( #This defines a ForeignKey relationship with the Project model, meaning each pledge is associated with a specific project.
      'Project', #This indicates that the Pledge model references the Project model (which might be defined elsewhere).
      on_delete=models.CASCADE, # This ensures that if a project is deleted, all related pledges will also be deleted (i.e., cascading deletion).
      related_name='pledges' #This allows you to access the pledges related to a project using project.pledges. For example, if you have a Project instance, you can get all related pledges by calling project.pledges.all().
  )
  supporter = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='pledges'
  )

 #