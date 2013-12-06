from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import  TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nuitinfo.views.home', name='home'),

    url(r'', include('APIHandler.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

