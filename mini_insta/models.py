#File: models.py
#Author: Nathan Moges (bmoges18@bu.edu) 10/3/25
#Description: The model.py creates the profile model and stores the user's info

from django.db import models
from django.urls import reverse


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
        return f"{self.display_name} on ig"

    def get_all_posts(self): 
        '''Return a QuerySet of posts for this profile.''' 
        posts = Post.objects.filter(profile=self) 
        return posts    
    
    def get_absolute_url(self):
        '''Return a URL to display one instance of this model.'''
        return reverse('show_profile', kwargs={'pk': self.pk})

    def get_followers(self):
        """Return a list of Profiles who follow this Profile."""
        followers = Profile.objects.filter(profile=self)
        profile_followers = []
        for follow in followers:
            profile_followers.append(follow.follower_profile)
        return profile_followers

    def get_num_followers(self):
        """Return the number of followers this Profile has."""
        return len(self.get_followers())
    
    def get_following(self):
        followers = Profile.objects.filter(follower_profile=self)
        profile_followers = []
        for follow in followers:
            profile_followers.append(follow.follower_profile)
        return profile_followers
    
    def get_num_following(self):
        return len(self.get_following())

    def get_post_feed(self):
        """Return a QuerySet of Posts made by the Profiles this Profile follows, most recent first."""
        from .models import Follow, Post
        following = Follow.objects.filter(follower_profile=self)
        followed_profiles = []
        for f in following:
            followed_profiles.append(f.profile)

        posts = Post.objects.filter(profile__in=followed_profiles).order_by("-timestamp")
        return posts

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of the Post model instance.'''
        return f"Here is my profile : {self.profile},  {self.caption},  {self.timestamp}"

    def get_all_photos(self):
        '''This accessor method will get all the photo objects that is specific to one profile'''
        photos = Photo.objects.filter(post=self)
        return photos

    def get_absolute_url(self):
        '''Return a URL to display one instance of this model.'''
        return reverse('show_post', kwargs={'pk': self.pk})

    def get_post_feed(self):
        '''Returns a list or QuerySet of Posts specifically  for the profiles being 
        followed by the profiles on which the method was called.'''
        

class Photo(models.Model):
    '''The photo model will model all the data attributes that are associated with the image that you will be posting.'''

    # Define the data attributes of the Photo object

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True)

    def get_image_url(self):
        '''Return the URL to this photo’s image.'''
        if self.image_url:
            return self.image_url
        elif self.image_file:
            return self.image_file.url
        else:
            return ''


    def __str__(self):
        '''Return a string representation of the Post model instance.'''
        return f"Here is my post : {self.post}, and what time I posted : {self.timestamp}"

class Follow(models.Model):
    '''Encapsulates the idea of an edge connecting two nodes within the social network.'''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "profile")
    follower_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "follower_profile")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of the fields from the Follow model.'''
        return f'{self.profile} follows: {self.follower_profile}'

class Comment(models.Model):
    '''Encapsulates the idea of one Profile providing a response or commentary on a Post.'''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)       
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(auto_now=True)               
    text = models.TextField(blank=False) 

    def get_all_comments(self):
        '''Return a QuerySet of all comments from a specific post.'''
        comments = Comment.objects.filter(post=self)
        return comments

    def __str__(self):
        '''Return a string representation of the fields from the Comment model.'''
        return f'{self.profile.username} commented on profile: {self.profile} saying {self.text}'
    
class Like(models.Model):
    '''Encapsulates the idea of one Profile providing a like on a Post.'''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)       
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(auto_now=True) 

    def get_likes(self):
        '''Return a QuerySet of all likes from a specific post.'''
        likes = Like.objects.filter(post=self)
        return likes

    def __str__(self):
        '''Return a string representation of the fields from the Like model.'''
        return f'{self.profile} liked your post: {self.post}'






