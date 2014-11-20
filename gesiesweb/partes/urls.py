from django.conf.urls import patterns, include, url

from .views import ParteListView, ParteCreateView, ParteDetailView, ParteUpdateView, ParteDeleteView,  ParteResponsableListView

urlpatterns = patterns("",
	url(regex=r'^$', view=ParteListView.as_view(), name="partes"),
    url(regex=r'^nuevo/$', view=ParteCreateView.as_view(), name="nuevo"),
    url(regex=r'^(?P<pk>\d+)/$', view=ParteDetailView.as_view(), name="detalle"),
    url(regex=r'^editar/(?P<pk>\d+)/$', view=ParteUpdateView.as_view(), name="editar"),
	url(regex=r'^responsable/$', view=ParteResponsableListView.as_view(), name="partes-responsable"),
    url(regex=r'^responsable/eliminar/(?P<pk>\d+)/$', view=ParteDeleteView.as_view(), name="eliminar"),
)