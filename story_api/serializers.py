from rest_framework import serializers 
from .models import Story 

class StorySerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Story # tell django which model to use
        fields = ('id', 'health', 'attack','accuracy','weapons','items','villains',) # tell django which fields to include
