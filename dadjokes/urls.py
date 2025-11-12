from django.urls import path
from .views import *

urlpatterns = [
    path('', RandomJokePictureView.as_view(), name="home"),
    path('random/', RandomView.as_view(), name="random"),
    path('jokes/', JokesListView.as_view(), name="show_all_jokes"),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name="show_joke"),
    path('pictures/', PicturesListView.as_view(), name="show_all_pictures"),
    path('picture/<int:pk>/', PictureDetailView.as_view(), name="show_picture"),

    #API
    path(r'api/', RandomJokeAPIView.as_view(), name="random_joke"),
    path(r'api/random/', RandomJokeDetailAPIView.as_view(), name=""),
    path(r'api/jokes/', JokeListAPIView.as_view(), name=""),
    path(r'api/joke/<int:pk>/', JokeDetailAPIView.as_view(), name=""),
    path(r'api/pictures/', PictureListAPIView.as_view(), name=""),
    path(r'api/picture/<int:pk>/', PictureDetailAPIView.as_view(), name=""),
    path(r'api/random_picture/', RandomPictureDetailAPIView.as_view(), name="random_picture"),
]