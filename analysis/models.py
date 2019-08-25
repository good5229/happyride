from django.db import models


# Create your models here.

class AreaModel(models.Model):
    class Meta:
        verbose_name = u'지역 운행횟수 데이터'
        ordering = ['name']

    name = models.CharField(verbose_name=u'지역명', max_length=256, blank=True, null=True)
    frequency_value = models.FloatField(verbose_name=u'운행횟수', blank=True, null=True)

    def __str__(self):
        return self.name + self.frequency_value
