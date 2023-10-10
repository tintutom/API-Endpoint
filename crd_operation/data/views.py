from django.shortcuts import render
from rest_framework import generics
from .serializers import ContentSerializer
from .models import Content

# Create your views here.

class CreateContent(generics.CreateAPIView):   #Create Content
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    
class ListContent(generics.ListAPIView):  #Get the Entire Content
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    
class Detailcontent(generics.RetrieveAPIView):  #Read Particular Content by id
    queryset = Content.objects.all()
    serializer_class =ContentSerializer
    
class DeleteContent(generics.DestroyAPIView):   #Delete Content
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    