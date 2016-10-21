from django.conf.urls import patterns, include, url
from log import views
urlpatterns = patterns('',
   
    url(r'^$', views.home, name='home'),
)
