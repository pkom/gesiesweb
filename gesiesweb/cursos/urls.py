from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns("",
	url(regex=r"^$",
		view=views.CursoListView.as_view(),
		name="curso"),
)