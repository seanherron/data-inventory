from django.db import models

import mimetypes

from datasets.models import Dataset

# Create your models here.

class Resource(models.Model):
    dataset = models.ForeignKey(Dataset)
    url = models.URLField("Link to the dataset")
    mime_type = models.CharField("MIME Type Format of the Dataset", max_length=250, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.access_url)
        
    def save(self, *args, **kwargs):
        # We're going to check to see if the file is being replaced, and if so, overwrite the old file rather than keep it laying around.
        try:
            self.mime_type = mimetypes.guess_type(self.url)[0]
        except:
            self.mime_type = "Unknown"
        
        super(Resource, self).save(*args, **kwargs)