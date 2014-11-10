from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns("",
	url(regex=r"^$",
		view=views.ConfigListView.as_view(),
		name="alumno"),


)