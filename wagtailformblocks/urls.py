from __future__ import unicode_literals

from django.conf.urls import url

from .views import FormProcessView

urlpatterns = [
    url(r'^submit/(?P<pk>\d+)/$', FormProcessView.as_view(),
        name='wagtailformblocks_process'),
]
