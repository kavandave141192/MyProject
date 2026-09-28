from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        
        fields=["id","username","password"] 
        # which fields has to be verified when request comes to backend

        extra_kwargs={"password":{"write_only":True}}
        # it tells to just put passwords on read only mode, not show while typing.. we tell Django to 
        # accept password but not return it.

    def create(self,validated_data):
        user= User.objects.create_user(**validated_data)
        return user    

#  serializers for model so we can receive and send json objects

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=["id","title","content","created_at","author"]
        extra_kwargs={"author":{"read_only":True}}