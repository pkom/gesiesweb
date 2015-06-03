from django.conf.urls import patterns, include, url

from .views import dame_grupos_curso

urlpatterns = patterns("",

    url(r"^ajax/dame_grupos_curso/$", dame_grupos_curso, name="dame_grupos_curso"),

)