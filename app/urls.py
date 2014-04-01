from django.conf.urls import patterns, include, url
import settings

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^', 'app.views.html2pdf'),
    
)


