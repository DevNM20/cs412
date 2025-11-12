# File: pictures.html
# Author: Nathan Moges (bmoges18@bu.edu) 11/11/25
# Description: This file show_all_pictures.html will display 
# all the pictures to the user
from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    '''
    A serializer for the Joke Model.
    Specify which model/fields to send in the API
    '''

    class Meta:
        model = Joke
        fields = ['name', 'text']

    def create(self, validated_data):
        '''
        Overide the superclass method that handles object creation.
        '''
        return Joke.objects.create(**validated_data)


class PictureSerializer(serializers.ModelSerializer):
    '''
    A serializer for the Picture Model
    Specify which model/fields to send in the API
    '''

    class Meta: 
        model = Picture 
        fields = ['name', 'image_url']

    def create(self, validated_data):
        '''
        Overide the superclass method that handles object creation.
        '''
        return Picture.objects.create(**validated_data)