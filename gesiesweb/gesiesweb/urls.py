from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

from core.views import HomeTemplateView, AboutTemplateView, LoginView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name='homeroot'),
    url(r'^login/$', LoginView.as_view(), name='loginroot'),
    url(r'^logout/$', 'core.views.mylogout', name='logoutroot'),
    url(r'^about/$', AboutTemplateView.as_view(), name='aboutroot'),
    # Examples:
    # url(r'^$', 'gesiesweb_project.views.home', name='home'),
    # url(r'^gesiesweb_project/', include('gesiesweb_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # urls main
    url(r'^core/',
        include('core.urls',
                namespace='core')),
    # urls configs
    url(r'^config/',
        include('config.urls',
                namespace='config')),
    # urls cursos 
    url(r'^cursos/',
        include('cursos.urls',
                namespace='curso')),

    # urls usuarios
    url(r'^profesores/',
        include('profesores.urls',
                namespace='profesor')),

    # urls alumnos
    url(r'^alumnos/',
        include('alumnos.urls',
                namespace='alumno')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # Uncomment the next line to serve media files in dev.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),)
