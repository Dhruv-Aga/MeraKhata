"""MeraKhata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from seller import views

app_name = 'seller'

urlpatterns = [
    url(r'^seller/$', views.SellerList.as_view(), name='list'),
    url(r'^seller/(?P<pk>[^/.]+)/', views.SellerDetail.as_view(), name='seller'),
]