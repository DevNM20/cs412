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
