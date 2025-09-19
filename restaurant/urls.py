
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