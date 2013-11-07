from django.db import models

from .fields import LanguageField

# Create your models here.

class Language(models.Model):
    language = LanguageField()
    
    def __unicode__(self):
        return u'%s' % (self.language)