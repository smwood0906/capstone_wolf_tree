"""wolf_tree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from beerfinder import views as bfviews
from sitepages.admin import user_admin_site
from blog import views as blogviews


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin2/', include(user_admin_site.urls)),
    url('^', include('sitepages.urls')),
    url(r'^beerfinder/?$', bfviews.bf),
    url(r'^news/?$', blogviews.post_list),
    url(r'^news/(?P<cat>[-\w]+)/(?P<slug>[-\w]+)/', blogviews.post, name='blog'),
    url(r'^events/', include('calendarium.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)