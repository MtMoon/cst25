from django.db import models
from photo.urls import wrap_photo_url, wrap_album_url

class Album(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField('Description', max_length=100)
    img = models.CharField(max_length=100, blank=True) 
    def __unicode__(self):
        return self.name
    def url(self):
        return wrap_album_url(self.id, 1)
    
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    desc = models.CharField('Description',max_length=100)
#    prev_id = models.IntegerField('Previous Photo ID')
#    next_id = models.IntegerField('Next Photo ID')
    album = models.ForeignKey('Album')
    def __unicode__(self):
        return self.image.url
    def img(self):
        return self.image.url
    def url(self):
        return wrap_photo_url(self.id)

class Comment(models.Model):
    uname = models.CharField('Author Name', max_length=16)
    text = models.CharField('Text', max_length=140)
    date = models.DateField('Date Published')
    photo = models.ForeignKey('Photo')
    def __unicode__(self):
        return "[{0}] {1}".format(self.uname, self.text[:10])
