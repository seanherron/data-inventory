# Create your views here.
from django.shortcuts import render_to_response

from .api.resources import ProgramCodeResource

def agency_list(request):
    res = ProgramCodeResource()
    request_bundle = res.build_bundle(request=request)
    queryset = res.obj_get_list(request_bundle)
    
    bundles = []
    for obj in queryset:
        bundle = res.build_bundle(obj=obj, request=request)
        
        bundles.append(res.full_dehydrate(bundle, for_list=True))
        
    list_json = res.serialize(None, bundles, "application/json")
    
    return render_to_response('omb_codes/agency_list.html', {
        "list_json": list_json,
    })