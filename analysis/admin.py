from django.contrib import admin

# Register your models here.
from analysis.models import AreaModel, BasicFeatures, Drive_Area


@admin.register(AreaModel)
class AreaModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'frequency_value')


@admin.register(BasicFeatures)
class BasicFeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'outside_people')


@admin.register(Drive_Area)
class Drive_Area(admin.ModelAdmin):
    list_display = ('name', 'text', 'wage', 'start_date')
