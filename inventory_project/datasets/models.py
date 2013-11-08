from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


from uuidfield import UUIDField
from model_utils import Choices

from publishers.models import Publisher
from omb_codes.models import Bureau_Code, Program_Code
from licenses.models import License
from languages.models import Language

# Create your models here.

class Tag(models.Model):
    name = models.CharField("Tag Name", max_length=50)
        
    def __unicode__(self):
        return u'%s' % (self.name)

class Category(models.Model):
    name = models.CharField("Category Name", max_length=50)
    
    def __unicode__(self):
        return u'%s' % (self.name)

class Dataset(models.Model):
    
    # Common Core Required Fields
    title = models.CharField("Title", help_text="Human-readable name of the asset. Should be in plain English and include sufficient detail to facilitate search and discovery.", max_length=250)
    description = models.TextField("Description", help_text="Human-readable description (e.g., an abstract) with sufficient detail to enable a user to quickly understand whether the asset is of interest.")
    tags = models.ManyToManyField(Tag)
    last_update = models.DateField("Last Update", help_text="Most recent date on which the dataset was changed, updated or modified.")
    publisher = models.ForeignKey(Publisher, help_text="The publishing agency")
    contact = models.ForeignKey(User, help_text="The Contact Person")
    unique_identifer = UUIDField(auto=True, unique=True)
    public_access_level_choices = Choices(('public', _('Public')), ('restricted', _('Restricted')), ('non_public', _('Non-Public')))
    public_access_level = models.CharField(choices=public_access_level_choices, max_length=50, default="public")
    
    # Common Core Required-if-Applicable Fields
    bureau_code = models.ForeignKey(Bureau_Code, help_text="Federal agencies, combined agency and bureau code from OMB Circular A-11, Appendix C in the format of 015:010.", blank=True, null=True)
    program_code = models.ForeignKey(Program_Code, help_text="Federal agencies, list the primary program related to this data asset, from the Federal Program Inventory. Use the format of 015:001", blank=True, null=True)
    access_level_comment = models.TextField(blank=True, help_text='An explanation for the selected "accessLevel" including instructions for how to access a restricted file, if applicable, or explanation for why a "non-public" or "restricted public" data assetis not "public", if applicable.', max_length=255)
    download_url = models.URLField(help_text="This must be the direct download URL. Use homepage for landing or disambiguation pages, or references for documentation pages. For multiple downloads, use distribution to include as many accessURL entries as you need.", blank=True)
    endpoint = models.URLField("Endpoint of web service to access dataset.", blank=True)
    license = models.ForeignKey(License, blank=True, null=True)
    spatial = models.TextField(help_text="The range of spatial applicability of a dataset. Could include a spatial region like a bounding box or a named place.", blank=True)
    temporal_start = models.DateField(help_text="The start of temporal applicability of the dataset", blank=True, null=True)
    temporal_end = models.DateField(help_text="The end of temporal applicability of the dataset", blank=True, null=True)
    
    # Common Core Expanded Fields
    categories = models.ManyToManyField(Category, blank=True, null=True)
    data_dictionary = models.URLField(help_text="URL to the data dictionary for the dataset or API. Note that documentation other than a data dictionary can be referenced using Related Documents as shown in the expanded fields.", blank=True)
    data_quality = models.NullBooleanField("Data Quality", help_text="Whether the dataset meets the agency's Information Quality Guidelines (true/false).")
    frequency_choices = Choices(('annual', _('Annual')), ('bimonthly', _('Bimonthly')), ('semiweekly', _('Semiweekly')), ('daily', _('Daily')), ('biweekly', _('biweekly')), ('semiannual', _('semiannual')), ('biennial', _('Biennial')), ('triennial', _('Triennial')), ('three-times-a-week', _('Three times a week')), ('three-times-a-month', _('Three times a month')), ('continuously-updated', _('Continuously updated')), ('monthly', _('Monthly')), ('quarterly', _('Quarterly')), ('semimonthly', _('Semimonthly')), ('three-times-a-year', _('Three times a year')), ('weekly', _('Weekly')), ('completely-irregular', _('Completely irregular')))
    frequency = models.CharField(choices=frequency_choices, max_length=50, blank=True)
    landing_page = models.URLField("Landing Page", help_text="This field is not intended for an agency's homepage (e.g. www.agency.gov), but rather if a dataset has a human-friendly hub or landing page that users should be directed to for all resources tied to the dataset. This allows agencies to better specify what a visitor receives after selecting one of the agency's datasets on Data.gov or in third-party mashups.", blank=True)
    languages = models.ManyToManyField(Language, blank=True, null=True)
    uii = models.CharField("Primary IT Investment UII", blank=True, max_length=75)
    release_date = models.DateTimeField("Date Issued", blank=True, null=True)
    sorn = models.URLField("Systems of Records Notice", blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.title)
    
class RelatedDocument(models.Model):
    dataset = models.ForeignKey(Dataset)
    url = models.URLField("URL", blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.url)
    