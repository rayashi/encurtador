from django.db import models

class Url(models.Model):
    url = models.URLField()
    count = models.IntegerField(blank=True,null=True,default=0)
