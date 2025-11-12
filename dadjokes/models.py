from django.db import models

# Create your models here.
class Joke(models.Model):
    '''Encapsulate the data of a Joke.'''

    #define the data attributes of the Article object
    text = models.TextField(blank=True)
    name = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance.'''
        return f'{self.text}: Created by: {self.name} and created at: {self.timestamp}'

class Picture(models.Model):
    '''Encapsulate the data of a Picture of a joke.'''
    image_url = models.URLField(blank=True)   
    name = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance.'''
        return f'{self.image_url} is a URL of the image, Created by: {self.name} and created at: {self.timestamp}'