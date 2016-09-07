from django.conf.urls import url
from sitepages import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^beers/?$', views.beers),
    url(r'^contact/?$', views.contact, name='contact'),
    url(r'^tumornator/?$', views.tumor),
    url(r'^staff/?$', views.staff),
    url(r'^brewery/?$', views.brewery),
    url(r'^farm/?$', views.farm),
    url(r'^all/?$', views.all),
    url(r'^subscribe/?$', views.subscribe),

]
