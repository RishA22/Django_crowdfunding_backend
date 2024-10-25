from django.apps import AppConfig


class UsersConfig(AppConfig): #This is a base class that is used to configure an app in Django
    default_auto_field = 'django.db.models.BigAutoField' #This specifies the type of auto-incrementing primary key field that will be used by default for models in this app
    name = 'users' #This sets the name of the app, which Django uses to identify it
