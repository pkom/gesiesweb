from django.conf.urls import patterns, url

from .views import HomeTemplateView, AboutTemplateView, ProfileDetailView, LoginView, mylogout, postprofile

urlpatterns = patterns('',
    url(r'^home/$', HomeTemplateView.as_view(), name='home'),
#    url(r'^login/$', mylogin, name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile'),
    url(r'^logout/$', mylogout, name='logout'),
    url(r'^about/$', AboutTemplateView.as_view(), name='about'),
)
