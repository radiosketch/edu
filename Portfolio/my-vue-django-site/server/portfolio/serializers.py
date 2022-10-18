from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ProjectDisplay, Post


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        # Specify the model we are using
        model = User
        # Specify the fields that should be made accessible.
        # Mostly it is all fields in that model
        fields = {
			'id', 'first_name', 'last_name', 'username',
			'password', 'is_active', 'is_superuser'
      	}


class ProjectDisplaySerializer(serializers.ModelSerializer):
	"""A serializer class for the ProjectDisplay model"""
	class Meta:
		# Specify the model we are using
		model = ProjectDisplay
		# Specify the fields that should be made accessible
		fields = {
			'id', 'title', 'description', 'link'
		}


class PostSerializer(serializers.ModelSerializer):
	"""A serializer for the Post model"""
	class Meta:
		# Specify the model we are using
		model = Post
		# Specify the fields that should be made accessible
		fields = '__all__'
