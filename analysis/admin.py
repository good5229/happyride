from django.contrib import admin

# Register your models here.
from analysis.models import AreaModel, BasicFeatures


@admin.register(AreaModel)
class AreaModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'frequency_value')


@admin.register(BasicFeatures)
class BasicFeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'bus_amount', 'distance', 'frequency', 'wage')
