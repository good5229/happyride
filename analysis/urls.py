from django.urls import path

from analysis.views import Select_Location, Introduce, Predict_Economic, Predict_Budget, Predict_User

app_name = 'analysis'

urlpatterns = [
    path('introduce/', Introduce.as_view(), name='intro'),
    path('select_location/', Select_Location.as_view(), name='select_loc'),
    path('predict_user/', Predict_User.as_view(), name='pre_user'),
    path('predict_budget/', Predict_Budget.as_view(), name='pre_bud'),
    path('predict_economic/', Predict_Economic.as_view(), name='pre_eco'),

]
