from django.urls import path

from .views import FormProcessView

urlpatterns = [
    path('submit/<int:pk>/', FormProcessView.as_view(), name='wagtailformblocks_process'),
]
