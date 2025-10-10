#File: views.py
# Author: Nathan Moges (bmoges18@bu.edu) 10/3/2025
# Description: This file views.py has three different views for the Profile and Post
# which are the ListView, DetaileView, and CreateView

from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
# Create your views here.
class ProfileListView(ListView):
    '''Defined a view class to show all Profiles.'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    '''Display a single Profile.'''

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

class PostDetailView(DetailView):
    '''Display a single Post'''

    model = Post 
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(CreateView):
    '''This view is used to make a new Post object.'''
    model = Post 
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''

        #calling the superclass method
        context = super().get_context_data()

        #find/add the post to the context data
        #retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        # add this post into the context dictionary:
        context['profile'] = profile
        return context


    def form_valid(self, form):
        '''This method handles the form submission and saves 
        the new object to the Django database. We need to add the foreign key 
        to the Post object before saving it to the database.'''

        print(form.cleaned_data)
        #retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get.filter(pk=pk)
        #attach this post to the profile
        form.instance.profile = profile

        post = form.save()

        # image_url = self.request.POST.get('image_url')
        # Photo.objects.create(post=post, image_url=image_url)

        files = self.request.FILES.getlist('files')   # "files" matches <input name="files">
        for f in files:
            Photo.objects.create(post=post, image_file=f)

        # delegate the work to the superclass method form_valid:
        return super().form_valid(form)
    
    def get_success_url(self):
        '''Provide a URL to redirect to after creating a new Post.'''
        #retrieve the PK from the URL patern
        pk = self.kwargs['pk']
        # call reverse to generate the URL for this Post
        return reverse('show_profile', kwargs={'pk': pk})

class UpdateProfileView(UpdateView):
    '''View class to handle update of a Profile based on its PK.'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

class UpdatePostView(UpdateView):
    '''View class to handle update of a Post based on its PK.'''
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''

        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        profile = Profile.objects.get(pk=self.object.profile.pk)

        context['post'] = post
        context['profile'] = profile

        return context

class DeletePostView(DeleteView):
    '''View class to delete a Post on an Profile.'''
    model = Post
    template_name = 'mini_insta/delete_post_form.html'

    def get_success_url(self):
        '''Return the URL to redirect to after a successful delete.'''

        #return the URL to redirect to:
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})
    
    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        profile = Profile.objects.get(pk=self.object.profile.pk)

        context['post'] = post
        context['profile'] = profile

        return context



    

