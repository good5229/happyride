from django.urls import path

from analysis.views import Select_Location, Introduce

app_name = 'analysis'

urlpatterns = [
    path('introduce/', Introduce.as_view(), name='intro'),
    path('select_location/', Select_Location.as_view(), name='select_loc'),
]
