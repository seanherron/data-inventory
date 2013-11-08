from django.conf.urls import patterns, url

from .views import DatasetListView, DatasetDetailView, DatasetCreateView, DatasetUpdateView, DatasetDeleteView

urlpatterns = patterns("",
    url(
        regex=r"^$",
        view=DatasetListView.as_view(),
        name="dataset_list"
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