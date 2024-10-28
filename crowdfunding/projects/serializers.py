from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer): #This defines a serializer class for the Pledge model. The ModelSerializer is a shortcut serializer that automatically generates fields based on the model.
  supporter = serializers.ReadOnlyField(source='supporter.id')
  class Meta: #The Meta class is used to define metadata for the PledgeSerializer, such as which model to use and which fields to include.
      model = apps.get_model('projects.Pledge') #This dynamically retrieves the Pledge model from the projects app using Django’s apps.get_model() function.
      fields = '__all__' #'__all__' tells the serializer to include all fields of the Pledge model. This means that every field defined in the Pledge model (e.g., amount, comment, anonymous, project) will be automatically included in the serialized output.
      #If you want to include only specific fields, you could list them as: fields = ['amount', 'comment', 'anonymous', 'project']

class ProjectSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.id') #This creates a read-only field in the serializer. It means the client cannot modify this field when creating or updating the object.The read-only field will only be included in the response data, not the request data, ensuring data integrity for fields that should not be altered by the client.
  #source specifies where to pull data from on the model. Here, owner is a foreign key field on the model, typically referencing the user who created the object. .id accesses the id of that related user instance, so owner.id will return the primary key (ID) of the user in the serialized data

  class Meta:
    model = apps.get_model('projects.Project')
    fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
  pledges = PledgeSerializer(many=True, read_only=True)

  def update(self, instance, validated_data):
    instance.project_name = validated_data.get('project_name', instance.project_name)
    instance.description = validated_data.get('description', instance.description)
    instance.goal = validated_data.get('goal', instance.goal)
    instance.image = validated_data.get('image', instance.image)
    instance.is_open = validated_data.get('is_open', instance.is_open)
    instance.create_date = validated_data.get('create_date', instance.create_date)
    instance.end_date = validated_data.get('end_date', instance.end_date)
    instance.owner = validated_data.get('owner', instance.owner)
    instance.save()
    return instance