from django.shortcuts import render
from django.views.generic import *
from .models import Joke, Picture
import random

# Create your views here.
# '' - show one Joke and one Picture selected at random
class RandomJokePictureView(DetailView):
    '''Display one Joke and one Picture selected at random.'''

    model = Joke
    template_name = "dadjokes/random_joke.html"
    context_object_name = "joke"

    def get_object(self):
        '''Return one instance of the Joke object selected at random.'''
        
        all_jokes = Joke.objects.all()
        joke = random.choice(all_jokes)
        return joke

    def get_context_data(self, **kwargs):
        '''Add one random Picture to the context.'''
        context = super().get_context_data(**kwargs)
        all_pictures = Picture.objects.all()
        picture = random.choice(all_pictures)
        context["picture"] = picture
        return context

# 'random' - show one Joke and one Picture selected at random
class RandomView(DetailView):
    '''Display one Joke and one Picture selected at random.'''

    model = Joke
    template_name = "dadjokes/random.html"
    context_object_name = "joke"

    def get_object(self):
        '''Return one instance of the Joke object selected at random.'''
        
        all_jokes = Joke.objects.all()
        joke = random.choice(all_jokes)
        return joke

    def get_context_data(self, **kwargs):
        '''Add one random Picture to the context.'''
        context = super().get_context_data(**kwargs)
        all_pictures = Picture.objects.all()
        picture = random.choice(all_pictures)
        context["picture"] = picture
        return context
        
# 'jokes' - show a page with all Jokes (no images)
class JokesListView(ListView):
    '''Define a view class to show all Jokes with no images.'''

    model = Joke
    template_name = "dadjokes/show_all_jokes.html"
    context_object_name = "jokes"

# 'joke/<int:pk>' - show one Joke by its primary key
class JokeDetailView(DetailView):
    '''Display a single Joke.'''

    model = Joke
    template_name = "dadjokes/joke.html"
    context_object_name = "joke"



# 'pictures' - show a page with all Pictures (no jokes)
class PicturesListView(ListView):
    '''Define a view class to show all Pictures with no jokes.'''

    model = Picture
    template_name = "dadjokes/show_all_pictures.html"
    context_object_name = "pictures"

# 'picture/<int:pk>' - show one Picture by its primary key
class PictureDetailView(DetailView):
    '''Display a single Picture.'''
    model = Picture 
    template_name = "dadjokes/picture.html"
    context_object_name = "picture"

############################################################
# Rest API

from rest_framework import generics
from .serializers import *

# 'api/' - returns a Json representation of one Joke selected at random
class RandomJokeAPIView(generics.ListAPIView):
    '''
    An API view to return one random Joke
    '''
    serializer_class = JokeSerializer

    def get_queryset(self):
        '''
        Return a queryset with one random Joke
        '''
        return [random.choice(Joke.objects.all())]

class RandomJokeDetailAPIView(generics.ListAPIView):
    '''
    An API view to return one random Joke
    '''
    serializer_class = JokeSerializer

    def get_queryset(self):
        '''
        Return a queryset with one random Joke
        '''
        return [random.choice(Joke.objects.all())]



# 'api/jokes' - returns a Json representation of all Jokes
class JokeListAPIView(generics.ListCreateAPIView):
    '''
    An API view to return a listing of Jokes
    '''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

# 'api/joke/<int:pk>' - returns a Json representation of one Joke by its primary key

class JokeDetailAPIView(generics.RetrieveAPIView):
    '''
    An API view to return one Joke by its primary key
    '''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


# 'api/pictures' - returns a Json representation of all Jokes
class PictureListAPIView(generics.ListCreateAPIView):
    '''
    An API view to return a listing of Jokes
    '''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

# 'api/picture/<int:pk>' - returns a Json representation of one Picture by its primary key
class PictureDetailAPIView(generics.RetrieveAPIView):
    '''
    An API view to return one Picture by its primary key
    '''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
