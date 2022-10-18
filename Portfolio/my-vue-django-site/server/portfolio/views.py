# portfolio/views.py

from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import ProjectDisplay, Post
from .serializers import UserSerializer, ProjectDisplaySerializer, PostSerializer

# Create your views here.

class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ProjectDisplayListCreate(generics.ListCreateAPIView):
	"""List and create Project Displays"""
	queryset = ProjectDisplay.objects.all()
	serializer_class = ProjectDisplaySerializer
	permission_classes = (permissions.IsAuthenticated, )


class ProjectDisplayRetrieveUpdate(generics.RetrieveUpdateAPIView):
	"""Retrieve and update Project Display information"""
	queryset = ProjectDisplay.objects.all()
	serializer_class = ProjectDisplaySerializer
	permission_classes = (permissions.IsAuthenticated, )


class PostListCreate(generics.ListCreateAPIView):
	"""List and create Posts"""
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.AllowAny, )


class PostRetrieveUpdate(generics.RetrieveUpdateAPIView):
	"""Retrieve and update Post information"""
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (permissions.AllowAny, )
