from django.db import models

# Create your models here.


class ItemModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='название', null=True)
    description = models.TextField(blank=True, verbose_name='описание')
    weight = models.FloatField(verbose_name='вес')