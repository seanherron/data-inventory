from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from omb_codes.models import Program_Code


class ProgramCodeResource(ModelResource):
    class Meta:
        queryset = Program_Code.objects.all()
        fields = ['agency','program_name']
        allowed_methods = ['get']
        serializer = Serializer()