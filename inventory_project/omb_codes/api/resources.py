from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.serializers import Serializer

from omb_codes.models import Program_Code, Bureau_Code


class ProgramCodeResource(ModelResource):
    def alter_list_data_to_serialize(self,request,data_dict): 
        if isinstance(data_dict,dict): 
            if 'meta' in data_dict: 
                del(data_dict['meta']) 
                return data_dict
    class Meta:
        queryset = Program_Code.objects.all()
        fields = ['agency','program_name', 'id']
        exclude = 'resource_uri'
        allowed_methods = ['get']
        serializer = Serializer()
        max_limit = None
        filtering = {
            'agency': ALL,
        }

class BureauCodeResource(ModelResource):
    def alter_list_data_to_serialize(self,request,data_dict): 
        if isinstance(data_dict,dict): 
            if 'meta' in data_dict: 
                del(data_dict['meta']) 
                return data_dict
    class Meta:
        queryset = Bureau_Code.objects.all()
        fields = ['branch','department', 'agency', 'agency_code', 'bureau_code', 'id']
        exclude = 'resource_uri'
        allowed_methods = ['get']
        serializer = Serializer()
        max_limit = None
        filtering = {
            'department': ALL,
        }