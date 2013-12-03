from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from tastypie.api import Api
from omb_codes.api.resources import ProgramCodeResource, BureauCodeResource
from datasets.api.resources import DatasetResource
#v1_api = Api(api_name='v1')
#v1_api.register(ProgramCodeResource())
#v1_api.register(BureauCodeResource())
#v1_api.register(DatasetResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'inventory_project.views.home', name='home'),
    # url(r'^inventory_project/', include('inventory_project.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    
    # API
    #(r'^api/', include(v1_api.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    (r'^selectable/', include('selectable.urls')),
    
    # User Logic URLs
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    
    # Dataset URLs
    url(r'^dataset/', include('datasets.urls')),
    
    # OMB Codes URLs
    url(r'^omb_codes/', include('omb_codes.urls')),
)
