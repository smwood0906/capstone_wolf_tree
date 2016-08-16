from django.conf.urls import url
from sitepages import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^beers/?$', views.beers),

]