"""MeraKhata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from commodity import views

app_name = 'commodity'

urlpatterns = [
    url(r'^item/$', views.ItemList.as_view(), name='list'),
    url(r'^item/(?P<pk>[^/.]+)/', views.ItemDetail.as_view(), name='item'),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[^/.]+)/', views.UserDetail.as_view()),
]