from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birth = models.DateField('Birthday')
    sex = models.BooleanField('Sex')
    signature = models.CharField('Signature', max_length=200)
    def __unicode__(self):
        return self.user.username
    def left(self):
        today = date(timezone.now().year,
                     timezone.now().month,
                     timezone.now().day)
        bdate = date(today.year, self.birth.month, self.birth.day)
        if bdate < today:
            bdate = date(today.year+1, self.birth.month, self.birth.day)
        return (bdate - today).days
    def username(self):
        return self.user.username
