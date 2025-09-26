from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data of a mini instagram.'''

    #define the data attributes of the Profile object
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    bio_text = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        '''return a string representation of this model instance.'''
        return f"My name is {self.display_name} but I go by {self.username} on ig"