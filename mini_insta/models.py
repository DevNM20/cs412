from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data of a mini instagram.'''

    #define the data attributes of the Profile object
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        '''return a string representation of this model instance.'''
        return f"This user's name is {self.display_name}, their username is {self.display_name}, he looks like this: {self.profile_image_url}, and he joined on {self.join_date}"