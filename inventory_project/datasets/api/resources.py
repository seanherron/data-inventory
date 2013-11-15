from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.serializers import Serializer

from datasets.models import Dataset


class DatasetResource(ModelResource):
    def alter_list_data_to_serialize(self,request,data_dict): 
        if isinstance(data_dict,dict): 
            if 'meta' in data_dict: 
                del(data_dict['meta']) 
                return data_dict
    class Meta:
        queryset = Dataset.objects.all()
        fields = ['title', 'description', 'tags', 'last_update', 'publisher', 'contact']
        exclude = 'resource_uri'
        allowed_methods = ['get']
        #serializer = Serializer()
        max_limit = None