from django.shortcuts import render, get_object_or_404
from .models import Post

app_name = 'blog'

from django.urls import path
from . import views
 
 
app_name = 'blog'
 
urlpatterns = [
     # post views
     path('', views.post_list, name='post_list'),
     path('<int:id>/', views.post_detail, name='post_detail'),
  ]