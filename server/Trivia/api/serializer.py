# Serializers allow complex data such as querysets and model instances 
# to be converted to native Python datatypes that can then be 
# easily rendered into JSON, XML or other content types

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
