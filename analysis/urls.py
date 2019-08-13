from django.urls import path

from analysis.views import Select_Location

app_name = 'analysis'

urlpatterns = [
    path('select_location/', Select_Location.as_view(), name='select_loc'),
]
