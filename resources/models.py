from django.db import models
from resources.urls import wrap_catalog_url

class Catalog(models.Model):
    name = models.CharField('Name',max_length=100)
    desc = models.CharField('Description', max_length=200)
    def __unicode__(self):
        return self.name
    def url(self):
        return wrap_catalog_url(self.id)

class ResFile(models.Model):
    name = models.CharField('Name', max_length=100)
    catalog = models.ForeignKey('Catalog', verbose_name='Catalog')
    rfile = models.FileField('File', upload_to='res/%Y/%m/%d')
    def __unicode__(self):
        return self.name
    def url(self):
        return self.rfile.url
