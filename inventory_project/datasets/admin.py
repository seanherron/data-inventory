from django.contrib import admin

import autocomplete_light

from .models import *
from languages.models import Language
from licenses.models import License
from omb_codes.models import Bureau_Code, Program_Code
from publishers.models import Publisher
from resources.models import Resource


class RelatedDocumentsInline(admin.TabularInline):
    model = RelatedDocuments

class ResourceInline(admin.TabularInline):
    model = Resource
    
class DatasetAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(Dataset)
    inlines = [
        RelatedDocumentsInline,
        ResourceInline,
    ]

    
admin.site.register(Dataset)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(License)
