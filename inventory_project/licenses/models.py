from django.db import models

# Create your models here.

class License(models.Model):
    title = models.CharField("License Name", max_length=125)
    url = models.URLField("URL to License Text")
    
    def __unicode__(self):
        return u'%s' % (self.title)