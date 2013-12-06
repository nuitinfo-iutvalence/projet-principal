from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nuitinfo.views.home', name='home'),
    url(r'^', include('APIHandler.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

