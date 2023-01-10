from django.shortcuts import render
from rest_framework import generics
from .serializers import StorySerializer
from .models import Story

class StoryList(generics.ListCreateAPIView):
    queryset = Story.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = StorySerializer # tell django what serializer to use

class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all().order_by('id')
    serializer_class = StorySerializer

# Create your views here.
