from django.conf.urls import patterns, include, url

from .views import ParteTemplateView, ParteResponsableTemplateView, ParteListView, ParteCreateView, ParteDetailView, ParteUpdateView
from .views import ParteResponsableListView, ParteResponsableBaseDatatableView, ParteDeleteView
from .views import grid_config, grid_handler, grid_config_responsable, grid_handler_responsable

urlpatterns = patterns("",
#   url(regex=r'^$', view=ParteListView.as_view(), name="partes"),
   url(regex=r'^profesor/$', view=ParteTemplateView.as_view(), name="partes-profesor"),
   url(regex=r'^responsable/$', view=ParteResponsableTemplateView.as_view(), name="partes-responsable"),
#   url(regex=r'^nuevo/$', view=ParteCreateView.as_view(), name="nuevo"),
#   url(regex=r'^(?P<pk>\d+)/$', view=ParteDetailView.as_view(), name="detalle"),
#   url(regex=r'^editar/(?P<pk>\d+)/$', view=ParteUpdateView.as_view(), name="editar"),
#   url(regex=r'^responsable/$', view=ParteResponsableListView.as_view(), name="partes-responsable"),
#   url(regex=r'^responsable/eliminar/(?P<pk>\d+)/$', view=ParteDeleteView.as_view(), name="eliminar"),
   url(regex=r'^responsable/data/$', view=ParteResponsableBaseDatatableView.as_view(), name='partes_responsable_json'),

   url(r'^partegrid/$', grid_handler, name='grid_handler'),
   url(r'^partegrid/cfg/$', grid_config, name='grid_config'),
   url(r'^partegridresponsable/$', grid_handler_responsable, name='grid_handler_responsable'),
   url(r'^partegridresponsable/cfg/$', grid_config_responsable, name='grid_config_responsable'),


)