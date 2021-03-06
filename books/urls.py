"""masteringdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from masteringdjango.views import (hello, current_datetime,
                                   hours_ahead)
from books.views import *


urlpatterns = [
    url(r'^list/$', BookLists.as_view(), name='user_books'),
    url(r'^create/$', CreateBook.as_view(), name='create_book'),
    url(r'^update/(?P<slug>[-\w]+)$', UpdateBook.as_view(), name='update_book'),

    url(r'^search_form/$', search_form),
    url(r'^search/$', search),
]

