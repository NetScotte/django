#encoding: utf-8

from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^create/', views.create, name='create'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'', views.liuyanlist, name='index')
]