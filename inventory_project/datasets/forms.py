from django import forms
from django.utils.translation import ugettext
from django.forms.models import modelformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, MultiField, HTML, Div
from crispy_forms.bootstrap import PrependedText, InlineField

import selectable.forms as selectable

from .models import Dataset, Tag
from resources.models import Resource


class DatasetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DatasetForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        # You can dynamically adjust your layout
        self.helper.layout = Layout(
            Div(
                Div(
                    Fieldset(
                        "Required Fields",
                        'title',
                        'description',
                        'tags',
                        'last_update',
                        'publisher',
                        'contact',
                        'public_access_level',
                        'access_level_comment'
                    ),
                    css_class='col-lg-6',
                ),
                Div(
                    Fieldset(
                        "Required-if-Applicable Fields",
                        Div(
                            'program_code',
                            'bureau_code',
                            css_id='federal_agency_codes'
                        ),
                        'download_url',
                        'endpoint',
                        'license',
                        'spatial',
                        'temporal_start',
                        'temporal_end',
                    ),
                    Fieldset(
                        "Expanded Fields",
                        'categories',
                        'data_dictionary',
                        'data_quality',
                        'frequency',
                        'landing_page',
                        'languages',
                        'uii',
                        'release_date',
                        'sorn',
                    ),
                    css_class="col-lg-6",
                ),
                css_class="row",
            )
        )           
    class Meta:
        model = Dataset
        widgets = {'tags': forms.CheckboxSelectMultiple, 'categories': forms.CheckboxSelectMultiple, 'languages': forms.CheckboxSelectMultiple}
        
class ResourceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        # You can dynamically adjust your layout
        self.helper.layout = Layout(
            Fieldset("Resources",
                'url'
            )
        )           
    class Meta:
        model = Resource
        

ResourceFormSet = modelformset_factory(Resource,
                                                fields=('url',),
                                                extra=2,
                                                form=ResourceForm)