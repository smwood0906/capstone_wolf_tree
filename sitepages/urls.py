from django.conf.urls import url
from sitepages import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^beers/?$', views.beers),
    url(r'^contact/?$', views.contact, name='contact'),
    url(r'^tumornator/?$', views.tumor),
    url(r'^about/?$', views.about),

]
