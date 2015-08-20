from django.db import models
from django.conf import settings


# Create your models here.
class Hikaye(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    parent= models.ForeignKey('self', null=True, blank=True, default=None)


