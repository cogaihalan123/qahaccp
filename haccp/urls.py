from django.conf.urls import patterns, url
from haccp import views
from django.conf import settings



urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^quaternary_form', views.QuatFormTechView, name='QuatFormTechView'),
    url(r'^quatform_list', views.QuatFormTodayView.as_view(), name='QuatFormTodayView'),
    url(r'^edit/(?P<pk>\d+)/$',views.QuatFormManView.as_view(), name="QuatFormManView"),
    )


if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )