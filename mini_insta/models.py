#File: models.py
#Author: Nathan Moges (bmoges18@bu.edu) 10/3/25
#Description: The model.py creates the profile model and stores the user's info

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

    def get_all_posts(self): 
        '''Return a QuerySet of posts for this profile.''' 
        posts = Post.objects.filter(profile=self) 
        return posts    




class Post(models.Model):
    '''Models the data attrivutes of our mini insta posts'''

    # Define the data attributes of the Post object

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of the Post model instance.'''
        return f"Here is my profile : {self.profile}, my caption : {self.caption}, and what time I posted : {self.timestamp}"

    def get_all_photos(self):
        photos = Photo.objects.filter(post=self)
        return photos

class Photo(models.Model):
    '''The photo model will model all the data attributes that are associated with the image that you will be posting.'''

    # Define the data attributes of the Photo object

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of the Post model instance.'''
        return f"Here is my post : {self.post}, image_url : {self.image_url}, and what time I posted : {self.timestamp}"



