from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie import fields, utils


from datasets.models import Dataset, Tag

class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        resource_name = "tags"
        include_resource_uri = True
        fields = ['name']

class DatasetResource(ModelResource):
    tags = fields.ToManyField(TagResource, 'tags', full=False, null=True)
    def alter_list_data_to_serialize(self,request,data_dict): 
        if isinstance(data_dict,dict): 
            if 'meta' in data_dict: 
                del(data_dict['meta']) 
                return data_dict
                
    class Meta:
        queryset = Dataset.objects.all()
        allowed_methods = ['get']
        include_resource_uri = False
        collection_name = 'datasets'
        serializer = Serializer()
        max_limit = None
        fields = ['title', 'description', 'tags', 'last_update', 'publisher', 'unique_identifer', 'public_access_level', 'bureau_code', 'program_code', 'access_level_comment', 'download_url', 'endpoint', 'license', 'spatial', 'temporal_start', 'temporal_end', 'categories', 'data_dictionary', 'data_quality', 'frequency', 'landing_page', 'languages', 'uii', 'release_date', 'sorn']