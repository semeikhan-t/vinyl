from django import serializer
from models import *

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User