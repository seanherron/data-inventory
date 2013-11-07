from django.db import models

# Create your models here.

class Publisher(models.Model):
    title = models.CharField("The name of the publishing entity", max_length=250)
    
    def __unicode__(self):
        return u'%s' % (self.title)