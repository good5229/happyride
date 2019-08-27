from django.db import models


# Create your models here.

class AreaModel(models.Model):
    class Meta:
        verbose_name = u'지역 운행횟수 데이터'
        ordering = ['name']

    name = models.CharField(verbose_name=u'지역명', max_length=256, blank=True, null=True)
    frequency_value = models.IntegerField(verbose_name=u'운행횟수', blank=True, null=True)

    def __str__(self):
        return self.name


class BasicFeatures(models.Model):
    class Meta:
        verbose_name = u'지역 기본자료'

    name = models.ForeignKey(AreaModel, on_delete=models.CASCADE, verbose_name=u'지역명', max_length=256,
                             blank=True, null=True)
    bus_amount = models.IntegerField(verbose_name=u'시내버스 대수', blank=True, null=True)
    distance = models.FloatField(verbose_name=u'거리', blank=True, null=True)
    frequency = models.IntegerField(verbose_name=u'운행횟수', blank=True, null=True)
    wage = models.IntegerField(verbose_name=u'요금', blank=True, null=True)
    outside_people = models.IntegerField(verbose_name=u'벽지노선 인구', blank=True, null=True)

    def __str__(self):
        return self.name.name


class Drive_Area(models.Model):
    class Meta:
        verbose_name = u'운영지역'

    name = models.ForeignKey(AreaModel, on_delete=models.CASCADE, verbose_name=u'지역명', max_length=256,
                             blank=True, null=True)
    start_date = models.CharField(verbose_name=u'시작 시기', max_length=64, blank=True, null=True)
    text = models.CharField(verbose_name=u'주요 특징', max_length=256, blank=True, null=True)
    wage = models.IntegerField(verbose_name=u'요금', blank=True, null=True)
    etc = models.CharField(verbose_name=u'기타 사항', max_length=256, blank=True, null=True)
