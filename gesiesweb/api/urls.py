from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import alumno_list, alumno_detail

urlpatterns = patterns(
    'api.views',
    url(r'^alumnos/$', alumno_list, name='alumno_list'),
    url(r'^alumnos/(?P<pk>[0-9]+)$', alumno_detail, name='alumno_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)