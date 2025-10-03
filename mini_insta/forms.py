from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''A form to add an Post to the database.'''

    class Meta:
        '''Associate this form with a model from our database.'''
        model = Post 
        fields = ['caption']
        