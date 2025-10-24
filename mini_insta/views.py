#File: views.py
# Author: Nathan Moges (bmoges18@bu.edu) 10/3/2025
# Description: This file views.py has three different views for the Profile and Post
# which are the ListView, DetaileView, and CreateView

from django.shortcuts import render
from django.db.models import Q
from django.views.generic import *
from django.urls import reverse
from .models import Profile, Post, Photo, Follow, Like
from .forms import CreatePostForm, CreateProfileForm, UpdateProfileForm, UpdatePostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mini_insta.models import Profile
from django.contrib.auth import login
from django.shortcuts import redirect




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

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')



class SearchView(LoginRequiredMixin, ListView):
    '''Adds a search featurre to our mini-insta'''
    model = Profile
    template_name = "mini_insta/search_results.html"
    context_object_name = "profiles"

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')
    
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

    def get_context_data(self, **kwargs):
        '''Give extra context for the current user's profile such as their follow status.'''
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        return context

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
        '''Handles the submission for both the profile form and the usercreationform.'''
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object() 
        return context

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

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')

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

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')


class UpdatePostView(LoginRequiredMixin, UpdateView):
    '''View class to handle update of a Post based on its PK.'''
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')

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

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')
    
    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        profile = Profile.objects.get(pk=self.object.profile.pk)

        context['post'] = post
        context['profile'] = profile

        return context

class FollowView(LoginRequiredMixin, DetailView):
    ''' View class that handles when a user follows a profile '''
    model = Profile
    template_name = "mini_insta/show_profile.html"

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')

    def post(self, request, pk, *args, **kwargs):
        '''Override the post method so when a user follows a page the user gets 
        redirected to the profile's page to see their follower count.'''
        user_profile = Profile.objects.get(user=request.user)
        other_profile = Profile.objects.get(pk=pk)

        if user_profile != other_profile:
            Follow.objects.get_or_create(
                profile=other_profile,
                follower_profile=user_profile
            )

        return redirect("show_profile", pk=other_profile.pk)


class DeleteFollowView(LoginRequiredMixin, DetailView):
    '''View class that handles the removing of the follow relationship for the logged-in user.'''
    model = Profile
    template_name = "mini_insta/show_profile.html"

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')

    def post(self, request, pk, *args, **kwargs):
        '''When the user unfollows this method will be called to delete that relationship between the two profiles.'''
        user_profile = Profile.objects.get(user=request.user)
        other_profile = Profile.objects.get(pk=pk)

        if user_profile != other_profile:
            Follow.objects.filter(
                profile=other_profile,
                follower_profile=user_profile
            ).delete()

        return redirect("show_profile", pk=other_profile.pk)

class LikePostView(LoginRequiredMixin, View):
    '''View class that adds the like on a post for the logged-in user.'''
    model = Post
    template_name = "mini_insta/show_post.html"

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')

    def post(self, request, pk, *args, **kwargs):
        '''Override the post method so when a user likes a post the user gets 
        redirected to the profile's page to see their like count.'''
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(pk=pk)

        # Prevent duplicate likes
        Like.objects.get_or_create(profile=profile, post=post)

        return redirect("show_post", pk=post.pk)


class DeleteLikeView(LoginRequiredMixin, DetailView):
    '''View class that handles the removing of the like on a post for the logged-in user.'''
    model = Post
    template_name = "mini_insta/show_post.html"

    def get_login_url(self):
        '''Return the URL for ths app's login page.'''
        return reverse('login')

    def post(self, request, pk, *args, **kwargs):
        '''When a user sends a POST request it will call this method to remove the like on the specific post.'''

        profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(pk=pk)

        # Remove like if exists
        Like.objects.filter(profile=profile, post=post).delete()

        return redirect("show_post", pk=post.pk)




    

