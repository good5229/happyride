# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from analysis.models import AreaModel, Drive_Area, BasicFeatures


class Introduce(TemplateView):
    template_name = 'analysis/introduce.html'


class Select_Location(TemplateView):
    template_name = 'analysis/select_location.html'


class Predict_User(TemplateView):
    template_name = 'analysis/predict_user.html'


class Drive_AreaView(DetailView):
    model = Drive_Area
    template_name = 'analysis/detail.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            city = request.GET['city']
            if city == "gunsan":
                city = "군산"
            elif city == "iksan":
                city = "익산"
            elif city == "gochang":
                city = "고창"
            elif city == "namwon":
                city = "남원"
            elif city == "muju":
                city = "무주"
            elif city == "buan":
                city = "부안"
            elif city == "sunchang":
                city = "순창"
            elif city == "wanju":
                city = "완주"
            elif city == "gimje":
                city = "김제"
            elif city == "jangsu":
                city = "장수"
            elif city == "imsil":
                city = "임실"
            elif city == "jeonju":
                city = "전주"
            elif city == "jeongeup":
                city = "정읍"
            elif city == "jinan":
                city = "진안"
        print(city)

        object = Drive_Area.objects.filter(name__name=city).first()
        context = {'city': city, 'start_date': object.start_date, 'wage': object.wage, 'text': object.text,
                   'etc': object.etc}
        return render(request, template_name='analysis/detail.html', context=context)


class Predict_Economic(TemplateView):
    template_name = 'analysis/predict_economic.html'


class Result_User(TemplateView):
    template_name = 'analysis/result_user.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            city = request.GET['city']
            if city == "gunsan":
                city = "군산"
            elif city == "iksan":
                city = "익산"
            elif city == "gochang":
                city = "고창"
            elif city == "namwon":
                city = "남원"
            elif city == "muju":
                city = "무주"
            elif city == "buan":
                city = "부안"
            elif city == "sunchang":
                city = "순창"
            elif city == "wanju":
                city = "완주"
            elif city == "gimje":
                city = "김제"
            elif city == "jangsu":
                city = "장수"
            elif city == "imsil":
                city = "임실"
            elif city == "jeonju":
                city = "전주"
            elif city == "jeongeup":
                city = "정읍"
            elif city == "jinan":
                city = "진안"

            city_object = AreaModel.objects.filter(name=city).first()
            forecast_user = city_object.frequency_value * 1.82
            context = {'city': city, 'forecast_drive': city_object.frequency_value,
                       'forecast_user': round(forecast_user, 3)}

            return render(request, template_name='analysis/result_user.html', context=context)


class Result_Economic(TemplateView):
    template_name = 'analysis/result_economic.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            city = request.GET['city']
            population = request.GET['population']
            normal_wage = request.GET['normal_wage']
            happy_wage = request.GET['happy_wage']
            bus = request.GET['bus']

            if city == "gunsan":
                city = "군산"
            elif city == "iksan":
                city = "익산"
            elif city == "gochang":
                city = "고창"
            elif city == "namwon":
                city = "남원"
            elif city == "muju":
                city = "무주"
            elif city == "buan":
                city = "부안"
            elif city == "sunchang":
                city = "순창"
            elif city == "wanju":
                city = "완주"
            elif city == "gimje":
                city = "김제"
            elif city == "jangsu":
                city = "장수"
            elif city == "imsil":
                city = "임실"
            elif city == "jeonju":
                city = "전주"
            elif city == "jeongeup":
                city = "정읍"
            elif city == "jinan":
                city = "진안"

            city_object = AreaModel.objects.filter(name=city).first()
            basic_feature = BasicFeatures.objects.filter(name=city_object).first()
            var_1_1 = population / basic_feature.outside_people * city_object.frequency_value * normal_wage - happy_wage
            var_2_1 = 60000000 * bus
            if var_1_1 > var_2_1:
                # 택시 비용이 더 큰 경우
                benifit = var_1_1 - var_2_1
                context = {'city': city, 'taxi_cost': var_1_1, 'bus_cost': var_2_1, 'benifit': benifit
                           'conclusion': '버스를 이용하는 것이 더 합리적입니다.'}

                return render(request, template_name='analysis/result_economic.html', context=context)
            elif var_2_1 > var_1_1:
                # 버스 비용이 더 큰 경우
                benifit = var_2_1 - var_1_1
                context = {'city': city, 'taxi_cost': var_1_1, 'bus_cost': var_2_1, 'benifit': benifit
                           'conclusion': '택시를 이용하는 것이 더 합리적입니다.'}

                return render(request, template_name='analysis/result_economic.html', context=context)
            else:
                # 두 비용이 같은 경우
                benifit = var_2_1 - var_1_1
                context = {'city': city, 'taxi_cost': var_1_1, 'bus_cost': var_2_1, 'benifit': benifit
                           'conclusion': '비용적으로 차이가 없습니다. 다른 요인을 고려해야 합니다.'}

                return render(request, template_name='analysis/result_economic.html', context=context)

