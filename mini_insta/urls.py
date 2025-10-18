# File: urls.py
# Author: Nathan Moges (bmoges18@bu.edu) 10/3/2025
# Description: This file urls.py maps the specific 
# paths of the different mini_insta pages, and the 
# individual one piece characters using the primary keys

from django.urls import path
from .views import *
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="show_profile"),
    path('profile/<int:pk>/followers/', ShowFollowersDetailView.as_view(), name="show_followers"),
    path('profile/<int:pk>/following/', ShowFollowingDetailView.as_view(), name="show_following"),
    path('profile/<int:pk>/create_post/', CreatePostView.as_view(), name="create_post"),
    path('profile/<int:pk>/update/', UpdateProfileView.as_view(), name="update_profile"),
    path('profile/<int:pk>/feed', PostFeedListView.as_view(), name="show_feed"),
    path('profile/<int:pk>/search', SearchView.as_view(), name="search"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="show_post"),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),
]