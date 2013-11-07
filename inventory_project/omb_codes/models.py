from django.db import models

# Create your models here.

class Bureau_Code(models.Model):
    branch = models.CharField("Branch of Government", max_length=250)
    agency = models.CharField("Agency", max_length=250)
    agency_code = models.CharField("OMB Agency Code", max_length=3)
    bureau_code = models.CharField("OMB Bureau Code", max_length=2)
    
    def __unicode__(self):
        return u'%s' % (self.agency)
    
class Program_Code(models.Model):
    agency = models.CharField("Agency", max_length=250)
    program_name = models.CharField(max_length=250)
    program_code = models.CharField(max_length=7)
    
    def __unicode__(self):
        return u'%s' % (self.program_name)