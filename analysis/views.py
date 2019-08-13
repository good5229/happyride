# Create your views here.
from django.views.generic import TemplateView


class Select_Location(TemplateView):
    template_name = 'analysis/select_location.html'
