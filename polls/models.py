from django.db import models

# Create your models here.
class vote(models.Model):
    liberals = models.IntegerField(default=0)
    conservative = models.IntegerField(default=0)
    ndp = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    public = models.IntegerField(default=0)
    bloc = models.IntegerField(default=0)

class voter(models.Model):
    voterId = models.CharField(max_length=15, null=True)
    casted = models.IntegerField(default=0)
    