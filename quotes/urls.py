
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static
from . import views 

# URL patterns specific to the quotes app:

urlpatterns = [
    # path(r'', views.home, name="home"),
    path(r'', views.home_page, name="home_page"),
    path(r'quote', views.home_page, name="quote_page"),
    path(r'show_all', views.show_all, name="show_all_page"),
    path(r'about', views.about, name="about_page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)