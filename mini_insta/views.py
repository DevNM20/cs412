#File: views.py
# Author: Nathan Moges (bmoges18@bu.edu) 10/3/2025
# Description: This file views.py has three different views for the Profile and Post
# which are the ListView, DetaileView, and CreateView

from django.shortcuts import render
from django.db.models import Q
from django.views.generic import *
from django.urls import reverse
from .models import Profile, Post, Photo, Follow
from .forms import CreatePostForm, CreateProfileForm, UpdateProfileForm, UpdatePostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mini_insta.models import Profile
from django.contrib.auth import login



# Create your views here.
class ProfileListView(ListView):
    '''Defined a view class to show all Profiles.'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class PostFeedListView(LoginRequiredMixin, ListView):
    '''This is the view for the feed page'''
    model = Post 
    template_name = "mini_insta/show_feed.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''

        #calling the superclass method
        context = super().get_context_data()

        #find/add the post to the context data
        #retrieve the PK from the URL pattern
        profile = self.get_object()

        # add this post into the context dictionary:
        context['profile'] = profile
        return context

    def get_object(self):
        '''return one instance of the Article object selected at random.''' 
        return Profile.objects.get(user=self.request.user)



class SearchView(LoginRequiredMixin, ListView):
    '''Adds a search featurre to our mini-insta'''
    model = Profile
    template_name = "mini_insta/search_results.html"
    context_object_name = "profiles"
    
    def dispatch(self, request, *args, **kwargs):
            '''override super method to handle any request'''

            profile = self.get_object()

            if 'query' not in request.GET:
                return render(request, 'mini_insta/search.html', {'profile': profile})
            else:
                return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        '''returns QuerySet of instance data for this search'''

        query = self.request.GET.get('query', '')
        return Post.objects.filter(caption__contains=query)

    def get_context_data(self):
        '''Return a dictionary containing context variables for use in this template'''
        context = super().get_context_data()

        profile = self.get_object()
        query = self.request.GET.get('query', '')

        context['profile'] = profile
        if query:

            context['query'] = query
            context['posts'] = self.get_queryset()
            context['profiles'] = Profile.objects.filter(
                Q(username__icontains=query) |
                Q(display_name__icontains=query) |
                Q(bio_text__icontains=query)
            )

        return context

    def get_object(self):
        '''return one instance of the Article object selected at random.'''
        
        return Profile.objects.get(user=self.request.user)

class ProfileDetailView(DetailView):
    '''Display a single Profile.'''

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

class CreateProfileView(CreateView):
    '''Used to make a new Profile object.'''
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_insta/create_profile_form.html"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
        context = super().get_context_data(**kwargs)
        context['new_user'] = UserCreationForm()
        return context
    
    def form_valid(self, form):
        user_form = UserCreationForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()

            login(self.request, user)

            form.instance.user = user

            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, user_creation_form=user_form)
            )
        


    

class PostDetailView(DetailView):
    '''Display a single Post'''

    model = Post 
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class ShowFollowersDetailView(DetailView):
    '''Display the followers'''

    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = "profile"

class ShowFollowingDetailView(DetailView):
    '''Display your following'''

    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = "profile"

class CreatePostView(LoginRequiredMixin, CreateView):
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
       
        profile = self.get_object()

        # add this post into the context dictionary:
        context['profile'] = profile
        return context


    def form_valid(self, form):
        '''This method handles the form submission and saves 
        the new object to the Django database. We need to add the foreign key 
        to the Post object before saving it to the database.'''

        print(form.cleaned_data)
        #retrieve the PK from the URL pattern
        profile = self.get_object()
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
        profile = self.get_object()
        # call reverse to generate the URL for this Post
        return reverse('show_profile', kwargs={profile.pk})
    def get_object(self):
        '''return one instance of the Article object selected at random.'''
        
        return Profile.objects.get(user=self.request.user)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    '''View class to handle update of a Profile based on its PK.'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def get_object(self):
        '''return one instance of the Article object selected at random.'''
        return Profile.objects.get(user=self.request.user)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    '''View class to handle update of a Post based on its PK.'''
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''

        context = super().get_context_data(**kwargs)
        pk = self.get_object()
        post = Post.objects.get(pk=pk)

        profile = Profile.objects.get(pk=self.object.profile.pk)

        context['post'] = post
        context['profile'] = profile

        return context

    def get_object(self):
        '''return one instance of the Article object selected at random.'''
        return Profile.objects.get(user=self.request.user)


class DeletePostView(LoginRequiredMixin, DeleteView):
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



    

