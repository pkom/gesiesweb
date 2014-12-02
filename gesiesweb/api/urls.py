from rest_framework import routers

from .views import CursoGrupoViewSet, GrupoAlumnoViewSet, ParteViewSet, ParteSeguimientoViewSet

router = routers.DefaultRouter()
router.register(r'cursogrupos', CursoGrupoViewSet)
router.register(r'grupoalumnos', GrupoAlumnoViewSet)
router.register(r'partes', ParteViewSet)
router.register(r'parteseguimientos', ParteSeguimientoViewSet)