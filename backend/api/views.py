from django.shortcuts import render

# This is Django's normal function for rendering HTML templates.
# For example:
# return render(request, "home.html")
# But your current API doesn't need it.
# Since you're building a React frontend + Django backend, you can remove it for now:

# added below two lines
from django.contrib.auth.models import User 
# Django already provides a built-in User model.You're importing that model so API can create/query users.

from rest_framework import generics
# You're importing DRF's generic API views.DRF provides ready-made classes for common operations:
# CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from .serializers import UserSerializer,NoteSerializer
# Go to serializers.py in this same app and import UserSerializer

from rest_framework.permissions import IsAuthenticated,AllowAny
#  Anybody can access this endpoint, even if they aren't logged in.

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all() 
    # This tells DRF:"This view works with the User model." User.objects.all() means:Get all User records.

    serializer_class=UserSerializer
    # User is your Django model.Whereas:UserSerializer is the serializer that tells DRF how to convert/validate the incoming data
    # I'm working with Users, and UserSerializer tells me how to process their API data.

    permission_classes=[AllowAny]

#  You're creating a new API endpoint whose purpose is:Create a new user.
# CreateAPIView is designed specifically for creating objects through an API, normally with a POST request.
# For example:

# POST /api/user/register

# with:

# {
#     "username": "kavan",
#     "password": "mypassword"
# }

class NoteListCreate(generics.ListAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)