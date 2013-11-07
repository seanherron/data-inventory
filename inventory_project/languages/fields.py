from django.db import models
from django.conf import settings
from django.utils import translation

from south.modelsinspector import add_introspection_rules


class LanguageField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        kwargs.setdefault('choices', [(k, translation.ugettext(v)) for k, v in settings.LANGUAGES])
        add_introspection_rules([], ["^languages\.fields\.LanguageField"])
        
        
        super(LanguageField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"