from django.urls import include, path

urlpatterns = [
    path('forms/', include('wagtailformblocks.urls')),
    path('', include('wagtail.core.urls')),
]
