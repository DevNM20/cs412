# File: urls.py
# Author: Nathan Moges (bmoges18@bu.edu), 9/12/2025
# Description: This is my urls.py file which maps all the urls to the correct view functions

from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static
from . import views 

# URL patterns specific to the quotes app:

urlpatterns = [
    path(r'quote', views.home_page, name="quote_page"),
    path(r'show_all', views.show_all, name="show_all_page"),
    path(r'about', views.about, name="about_page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)