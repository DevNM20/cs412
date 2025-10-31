# marathon_analytics/urls.py

from django.urls import path 
from . import views 

urlpatterns = [
    path(r'', views.ResultsListView.as_view(), name='home'),
    path(r'results', views.ResultsListView.as_view(), name='results_list'),
    path(r'result/<int:pk>', views.ResultsDetailView.as_view(), name='result_detail'),
]