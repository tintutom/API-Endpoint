from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=100,blank=False,unique=True)
    description = models.CharField(max_length=255,blank=False)
    
    def __str__(self):
        return self.title