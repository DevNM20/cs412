#File: views.py
# Author: Nathan Moges (bmoges18@bu.edu) 9/26/2025
# Description: This file views.py has two classes one of them being 
# provide us all the Profile objects and the other class displays the Profile

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
# Create your views here.
class ProfileListView(ListView):
    '''Defined a view class to show all Profiles.'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    '''Display a single Profile.'''

    model = Profile
    template_name = "mini_insta/profile.html"
    context_object_name = "profile"
