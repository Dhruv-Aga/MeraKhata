# """MeraKhata URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.11/topics/http/urls/
# """
# # Django imports
# from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^commodity/', include('commodity.urls', namespace='commodity')),
    url(r'^seller/', include('seller.urls', namespace='seller')),
    url(r'^admin/', admin.site.urls),
]