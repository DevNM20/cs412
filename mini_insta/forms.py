# File: forms.py
# Author: Nathan Moges (bmoges18@bu.edu) 10/3/2025
# Description: The file forms.py defines the forms that we will use for create/update/delete operations

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''A form to add an Post to the database.'''

    class Meta:
        '''Associate this form with a model from our database.'''
        model = Post 
        fields = ['caption']
        