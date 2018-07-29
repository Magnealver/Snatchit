"""
Definition of urls for django_gw2_snatchit.
"""

from django.conf.urls import include, url
import DefaultTool.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', django_gw2_snatchit.views.home, name='home'),
    # url(r'^django_gw2_snatchit/', include('django_gw2_snatchit.django_gw2_snatchit.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', DefaultTool.views.index, name='index'),
    url(r'^home$', DefaultTool.views.index, name='home'),
]
