from django.conf.urls import patterns, url

from APIHandler import views

urlpatterns = patterns('',
    #url(r'^$', views.item, name='item'), //TODO: Change 
    url(r'^category/(?P<pk>\d+)/$', views.send_category, name='category_detail'),
    #[^/] every char unless '/', 
    url(r'^product/(?P<pk>\d+)/$', views.send_product, name='product_detail')    
)