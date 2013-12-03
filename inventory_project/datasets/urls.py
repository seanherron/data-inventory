from django.conf.urls import patterns, url, include

from rest_framework import routers

from .views import DatasetListView, DatasetDetailView, DatasetCreateView, DatasetUpdateView, DatasetDeleteView, DataJsonView, DatasetViewSet, TagDetailView

router = routers.DefaultRouter()
router.register(r'datasets', DatasetViewSet)

urlpatterns = patterns("",
    url(r'^', include(router.urls)),
    url(r'^tags/(?P<pk>[0-9]+)/$',
        TagDetailView.as_view(),
        name='tag-detail'
    ),
    url(
        regex=r"^$",
        view=DatasetListView.as_view(),
        name="dataset_list"
    ),
    url(
        regex=r"^data.json",
        view=DataJsonView.as_view(),
        name="dataset_json"
    ),
    url(
        regex=r"^create/$",
        view=DatasetCreateView.as_view(),
        name="dataset_create"
    ),
    url(
        regex=r"^(?P<slug>\w+)/$",
        view=DatasetDetailView.as_view(),
        name="dataset_detail"
    ),
    url(
        regex=r"^(?P<slug>\w+)/update/$",
        view=DatasetUpdateView.as_view(),
        name="dataset_update"
    ),
    url(
        regex=r"^(?P<slug>\w+)/delete/$",
        view=DatasetDeleteView.as_view(),
        name="dataset_delete"
    ),
    
)