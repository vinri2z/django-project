from django.conf.urls import url

from . import views  # import views so we can use them in urls.

urlpatterns = [
    url(r'^listing/', views.listing),
    url(r'^search/', views.search),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
]
