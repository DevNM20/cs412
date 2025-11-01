# File: urls.py
# Author: Nathan Moges (bmoges18@bu.edu) 10/31/2025
# Description: This file urls.py maps the specific 
# paths of the different pages of our app 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.VoterListView.as_view(), name='voter_list'),
    path('voter/<int:pk>/', views.VoterDetailView.as_view(), name='voter_detail'),
]