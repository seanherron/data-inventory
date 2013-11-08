from django.contrib import admin

from django import forms

import selectable
from selectable.forms import AutoCompleteSelectField, AutoCompleteSelectMultipleField

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

from .models import *
from .lookups import UserLookup

from languages.models import Language
from licenses.models import License

from omb_codes.models import Bureau_Code, Program_Code
from omb_codes.lookups import ProgramCodeLookup, BureauCodeLookup

from publishers.models import Publisher
from resources.models import Resource

class RelatedDocumentsInline(admin.TabularInline):
    model = RelatedDocument

class ResourceInline(admin.TabularInline):
    model = Resource
    
class BureauCodeField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if obj.department:
            return "%s -- %s" % (obj.department, obj.agency)
        else:
            return "%s" % (obj.agency)
            
class ProgramCodeField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s -- %s" % (obj.agency, obj.program_name)

class DatasetAdminForm(forms.ModelForm):
    bureau_code = AutoCompleteSelectField(lookup_class=BureauCodeLookup)
    program_code = AutoCompleteSelectField(lookup_class=ProgramCodeLookup)
    contact = AutoCompleteSelectField(lookup_class=UserLookup, allow_new=True)
    
    class Meta:
        model = Dataset
    
    def __init__(self, *args, **kwargs):
        super(DatasetAdminForm, self).__init__(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        program_code = self.cleaned_data['program_code']
        self.instance.program_code = program_code
        return super(DatasetAdminForm, self).save(*args, **kwargs)
        
    class Media:
        css = {
            "all": ("css/admin.css",)
        }
    
class DatasetAdmin(admin.ModelAdmin):
    form = DatasetAdminForm
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
