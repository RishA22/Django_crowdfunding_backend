from rest_framework.views import APIView #This imports APIView from the DRF. APIView is a class-based view in DRF that allows you to define your HTTP request methods (like GET, POST, etc.). It provides the structure for handling API requests in a more organized manner.
from rest_framework.response import Response #This imports Response from the DRF. Response is used to return HTTP responses from your API views. It helps you format the data in the correct format (e.g., JSON) for the client to consume.
from rest_framework import status, permissions #imports the status module from Django REST Framework (DRF), which contains a set of standard HTTP status codes. These codes help you define appropriate responses for different outcomes of your API views.
from .models import Project, Pledge #This imports the Project and Pledge model from the models.py file in the current app. Models represent the structure of the data (e.g., a project in the crowdfunding platform).
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer #This imports the ProjectSerializer,PledgeSerializer and ProjectDetailSerializer from the serializers.py file in the current app. A serializer is used to convert complex data types like Django models into Python data types (or JSON) that can be rendered into responses, and vice versa
from django.http import Http404 #imports the Http404 exception class from Django's http module. This class is used to raise a "404 Not Found" error when a resource (such as a model instance or page) cannot be found in a view.
from .permissions import IsOwnerOrReadOnly

class ProjectList(APIView): #This defines a new class called ProjectList that inherits from APIView. It will handle requests related to listing Project instances.
  
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def get(self, request): #This defines a GET method for the ProjectList class, which handles GET requests (retrieving data).
    projects = Project.objects.all() #This line fetches all the instances of the Project model from the database using Django's ORM (objects.all()).
    serializer = ProjectSerializer(projects, many=True) #This creates a ProjectSerializer instance to serialize the list of Project objects (the many=True argument tells the serializer to handle multiple objects).
    return Response(serializer.data) #This returns the serialized data (in JSON format) as a response to the client.
  
  def put(self, request, pk):
    project = self.get_object(pk)
    serializer = ProjectDetailSerializer(
        instance=project,
        data=request.data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
  
  def post(self, request): #This defines the POST method for the view, which will handle requests to create new data. The request object contains data sent by the client in the HTTP request body (usually in JSON format).
      serializer = ProjectSerializer(data=request.data) #This initializes the ProjectSerializer with the data sent in the request (request.data). The ProjectSerializer will validate the data to ensure it meets the requirements for creating a new Project.
      if serializer.is_valid(): #This checks if the data provided is valid according to the rules defined in the ProjectSerializer (e.g., required fields, data types).
          serializer.save(owner=request.user) #If the data is valid, this saves the new Project instance to the database. The save() method is automatically provided by the serializer.
          return Response(
              serializer.data,
              status=status.HTTP_201_CREATED #If the data is valid and the Project is saved, this returns the serialized data of the newly created Project in the response, along with a status code of 201 Created, indicating successful creation.
          )
      return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST #If the data is not valid, this returns the errors generated by the serializer (which explain what went wrong), along with a 400 Bad Request status code, indicating that the client made an invalid request.
      )
  
class PledgeList(APIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get(self, request):
      pledges = Pledge.objects.all()
      serializer = PledgeSerializer(pledges, many=True)
      return Response(serializer.data)

  def post(self, request):
      serializer = PledgeSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(
              serializer.data,
              status=status.HTTP_201_CREATED
          )
      return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
      )
  
class ProjectDetail(APIView): #This creates a class-based view named ProjectDetail that inherits from APIView. It handles operations on a single Project instance (i.e., detail view).

    permission_classes = [
   permissions.IsAuthenticatedOrReadOnly,
   IsOwnerOrReadOnly
]
    def get_object(self, pk): #This method is used to retrieve a Project object based on its primary key (pk)
        try: #: It attempts to fetch the Project object from the database using Project.objects.get(pk=pk), where pk is the unique identifier for the project.
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return Project.objects.get(pk=pk) #If the Project exists, it is returned.
        except Project.DoesNotExist: #If the Project with the given pk does not exist, it raises an Http404 exception, which tells the client that the requested resource was not found.
            raise Http404

    def get(self, request, pk): #This method handles GET requests to retrieve the details of a specific Project.
        project = self.get_object(pk) #project = self.get_object(pk): It calls the get_object method to fetch the Project object with the specified pk. If the object doesn't exist, it will raise a 404 error.
        serializer = ProjectDetailSerializer(project) #It passes the project object to the ProjectSerializer to convert it into a serialized format (e.g., JSON) suitable for an API response.
        return Response(serializer.data) #It returns the serialized data as a JSON response to the client.
    
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
        instance=project,
        data=request.data,
        partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )
    
    #Add a delete method (exercise)
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()  # Deletes the project from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Responds with a 204 status code