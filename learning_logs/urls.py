"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all topics.
    path(r'topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # url for new topics
    path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Page to edit entries
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]




