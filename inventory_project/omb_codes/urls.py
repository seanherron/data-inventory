from django.conf.urls.defaults import *

from .views import agency_list

urlpatterns = patterns("",
    url(r"^agency_list/$", 'omb_codes.views.agency_list'),
)