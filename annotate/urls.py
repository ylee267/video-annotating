from django.conf.urls import patterns, url
from annotate.views import AnnotationView, UserView

urlpatterns = patterns('',
    url(r'^process/', AnnotationView.as_view(), name='process'),
    url(r'^$', UserView.as_view(), name='start'),
)
