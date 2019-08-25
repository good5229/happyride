# Create your views here.


from django.views.generic import TemplateView


class Introduce(TemplateView):
    template_name = 'analysis/introduce.html'


class Select_Location(TemplateView):
    template_name = 'analysis/select_location.html'


class Predict_User(TemplateView):
    template_name = 'analysis/predict_user.html'

    def form_valid(self, form):
        instance = form.instance
        return super().form_valid(form)


class Predict_Budget(TemplateView):
    template_name = 'analysis/predict_budget.html'


class Predict_Economic(TemplateView):
    template_name = 'analysis/predict_economic.html'
