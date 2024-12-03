# Serializers allow complex data such as querysets and model instances 
# to be converted to native Python datatypes that can then be 
# easily rendered into JSON, XML or other content types

#present data fields from models.py that i want to expose via the api

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Quiz, GameStats

# serializer for the User model to handle serialization & deserialization
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password'] # The fields to include in the serialized output
        extra_kwargs = {'password': {'write_only': True}} # write_only for security reasons

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz 
        fields = ['question', 'optionOne', 'optionTwo', 'optionThree','answer'] 

class GameStatsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True) #the username is from user model

    class Meta:
        model = GameStats
        fields = ['username', 'score']

