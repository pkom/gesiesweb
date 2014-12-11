from rest_framework.routers import DefaultRouter

from .views import CursoGrupoViewSet, GrupoAlumnoViewSet, ParteViewSet, ParteSeguimientoViewSet

router = DefaultRouter()
router.register(r'cursogrupos', CursoGrupoViewSet)
router.register(r'grupoalumnos', GrupoAlumnoViewSet)
router.register(r'partes', ParteViewSet)
router.register(r'parteseguimientos', ParteSeguimientoViewSet)