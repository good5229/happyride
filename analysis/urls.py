from django.urls import path

from analysis.views import Select_Location, Introduce, Predict_Economic, Predict_User, Result_User, \
    Result_Economic, Drive_AreaView

app_name = 'analysis'

urlpatterns = [
    path('introduce/', Introduce.as_view(), name='intro'),
    path('select_location/', Select_Location.as_view(), name='select_loc'),
    path('predict_user/', Predict_User.as_view(), name='pre_user'),
    path('predict_economic/', Predict_Economic.as_view(), name='pre_eco'),
    path('result_user/', Result_User.as_view(), name='result_user'),
    path('result_economic/', Result_Economic.as_view(), name='result_eco'),
    path('detail', Drive_AreaView.as_view(), name='detail'),
]
