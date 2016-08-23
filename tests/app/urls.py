from django.conf.urls import include, url

from wagtail.wagtailcore import urls as wagtail_urls

from wagtailformblocks import urls as formblocks_urls

urlpatterns = [
    url(r'^forms/', include(formblocks_urls)),
    url(r'', include(wagtail_urls)),
]
