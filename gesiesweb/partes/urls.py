from django.conf.urls import patterns, include, url

from .views import PartesListView, PartesResponsableListView, PartesDetailView

urlpatterns = patterns("",
	url(regex=r'^$', view=PartesListView.as_view(), name="partes"),
	url(regex=r'^responsable/$', view=PartesResponsableListView.as_view(), name="partes-responsable"),
    url(regex=r'^(?P<pk>\d+)/$', view=PartesDetailView.as_view(), name="detalle"),
)