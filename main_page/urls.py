from django.conf.urls import url, include
from django.contrib import admin
from main_page import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact')
]

