# File: urls.py
# Author: Nathan Moges (bmoges18@bu.edu) 9/19/2025
# Description: This file urls.py has maps the specific 
#paths of main, order, and confirmation pages

from django.urls import path
from django.conf import settings 
from . import views 

app_name = 'restaurant'
# Url patterns for this app
urlpatterns = [
    path(r'', views.show_main, name='show_main'),
    path(r'main', views.show_main, name='show_main'),
    path(r'order', views.submit_order, name='order'),
    path(r'confirmation', views.confirmation, name='confirmation') 
]