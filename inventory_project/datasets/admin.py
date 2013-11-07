from django.contrib import admin

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

from .models import *
from languages.models import Language
from licenses.models import License
from omb_codes.models import Bureau_Code, Program_Code
from publishers.models import Publisher
from resources.models import Resource

class RelatedDocumentsInline(admin.TabularInline):
    model = RelatedDocument

class ResourceInline(admin.TabularInline):
    model = Resource
    
class DatasetAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', 'categories', )
    inlines = [
        RelatedDocumentsInline,
        ResourceInline,
    ]
    fieldsets = (
            ('Common Core Required', {
                'fields': ('title', 'description', 'tags', 'last_update', 'publisher', 'contact', 'public_access_level')
            }),
            ('Required-if-Applicable', {
                'fields': ('bureau_code', 'program_code', 'access_level_comment', 'download_url', 'endpoint', 'license', 'spatial', 'temporal_start', 'temporal_end')
            }),
            ('Expanded', {
                'fields': ('categories', 'data_dictionary', 'frequency', 'landing_page', 'languages', 'uii', 'release_date', 'sorn')
            }),
        )

    
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Resource)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(License)
