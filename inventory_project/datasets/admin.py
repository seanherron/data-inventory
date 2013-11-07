from django.contrib import admin

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
    #readonly_fields = ('uuid',)
    inlines = [
        RelatedDocumentsInline,
        ResourceInline,
    ]
    exclude = ('')

    
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(License)
