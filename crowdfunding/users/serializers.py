from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer): #A DRF class that automatically creates a serializer with fields and validation rules that match a Django model.
    class Meta:
        model = CustomUser #Specifies the model that this serializer is based on, which is CustomUser.
        fields = '__all__' #This includes all fields from CustomUser in the serializer output.
        extra_kwargs = {'password': {'write_only': True}} #This setting makes the password field write-only, meaning it can be sent to the API but won’t be included in the response data. This is important for security, so user passwords aren't exposed in API responses.

    def create(self, validated_data): #This method is used instead of create because it automatically hashes the password. create_user is a method on Django’s user manager that ensures the password is stored securely.
        return CustomUser.objects.create_user(**validated_data)
    #This ensures validated_data is cleaned, validated, and ready to be used directly in methods like create() and update()