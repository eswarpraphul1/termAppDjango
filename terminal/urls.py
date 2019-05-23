
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^cmd-json/', views.event_cmd_json, name='event_cmd_json'),
    url(r'^wed-json/', views.event_wed_json, name='event_wed_json'),
    url(r'^init-json/', views.event_init_json, name='event_init_json'),
    url(r'^', views.index, name='index'),
]