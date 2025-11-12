# blog/serializers.py
# Serializers convert our django data models to a 
# text-representation suitable to transmit over HTTP 

from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    '''
    A serializer for the Article Model.
    Specify which model/fields to send in the API
    '''

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'text']
    
    #add methods to customizer the Create/Read/Update/Delete operations

    def create(self, validated_data):
        '''
        overide the superclass method that handles object creation.
        '''
        print(f'ArticleSerializer.creaate, validated_data={validated_data}.')

        #create an Article object\
       # article = Article(**validated_data)
        #attach a Foreign Key for the User
       # article.user = User.objects.first()
        # save the object to the database
       # article.save()
        #return an object instance
        #return article

        # a simplified way: 
        #attach a foreign key for the user 
        validated_data['user'] = User.objects.first()
        # do the create and save all at once 
        return Article.objects.create(**validated_data)

