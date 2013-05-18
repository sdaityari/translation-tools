from django.db import models
from poeditor import custom_models as custom

import os.path

class PoFile(models.Model):
    name = models.CharField(max_length = 50)
    po = custom.AutoDeleteFileField(upload_to='test/')
    
    def __unicode__(self):
        return self.name

class PoMessages(models.Model):
    po_file = models.ForeignKey(PoFile)
    location = models.TextField(blank = True)
    source = models.TextField(blank = True)
    target = models.TextField(blank = True)
    
    def __unicode__(self):
        return str(self.po_file.name) + ":" + str(self.location)
