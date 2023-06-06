from django.db import models

# Create your models here.


class ProcessingImage(models.Model):
    sourceFile = models.ImageField()
    radioValue = models.CharField(default='TestValue', max_length=30)
    # name = models.CharField('Image name', max_length=20)
    # outputFile = models.FileField('Output Image File', max_length=254)
