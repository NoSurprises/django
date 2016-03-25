from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    
    url(r'^$', views.home, name='home'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/plus/$', views.plus, name='plus'),
    url(r'^(?P<slug>[\w-]+)/minus/$', views.minus, name='minus'),
]
