from django.conf.urls import patterns, include, url

from .views import ConfigListView, dame_alumnos_curso

urlpatterns = patterns("",
    url(regex=r"^$", view=ConfigListView.as_view(), name="alumno"),

    url(r"^ajax/dame_alumnos_curso/$", dame_alumnos_curso, name="dame_alumnos_curso"),

)