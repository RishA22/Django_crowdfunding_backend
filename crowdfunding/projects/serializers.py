from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer): #This defines a serializer class for the Pledge model. The ModelSerializer is a shortcut serializer that automatically generates fields based on the model.
  class Meta: #The Meta class is used to define metadata for the PledgeSerializer, such as which model to use and which fields to include.
      model = apps.get_model('projects.Pledge') #This dynamically retrieves the Pledge model from the projects app using Django’s apps.get_model() function.
      fields = '__all__' #'__all__' tells the serializer to include all fields of the Pledge model. This means that every field defined in the Pledge model (e.g., amount, comment, anonymous, project) will be automatically included in the serialized output.
      #If you want to include only specific fields, you could list them as: fields = ['amount', 'comment', 'anonymous', 'project']

class ProjectSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.id')

  class Meta:
    model = apps.get_model('projects.Project')
    fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
  pledges = PledgeSerializer(many=True, read_only=True)

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.goal = validated_data.get('goal', instance.goal)
    instance.image = validated_data.get('image', instance.image)
    instance.is_open = validated_data.get('is_open', instance.is_open)
    instance.date_created = validated_data.get('date_created', instance.date_created)
    instance.owner = validated_data.get('owner', instance.owner)
    instance.save()
    return instance