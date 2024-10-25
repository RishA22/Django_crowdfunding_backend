from django.contrib.auth.models import AbstractUser
from django.db import models  # Import models

class CustomUser(AbstractUser): #This imports Django's AbstractUser class, which is a base class for creating custom user models, AbstractUser already includes basic functionality for authentication, such as username, password, email, and other common fields.
  bio = models.TextField(blank=True, null=True) # Added bio field

  #username =
  #email = 
  #password =
  
  def __str__(self): #This is a special method in Python that defines how the object is represented as a string. In this case, when you print a CustomUser object (or use it in places where a string is required), it will return the username of the user.
      return self.username
