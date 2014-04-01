from django.conf.urls import patterns, include, url
import settings

urlpatterns = patterns('',
    url(r'^', 'app.views.html2pdf'),
)


