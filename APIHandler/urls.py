from django.conf.urls import patterns, url

from APIHandler import views

urlpatterns = patterns('',
    url(r'^$', views.item, name='item')
)