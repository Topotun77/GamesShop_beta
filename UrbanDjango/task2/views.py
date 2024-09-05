from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_(request):
    return render(request, 'second_task/func_template.html')


class class_(TemplateView):
    template_name = 'second_task/class_template.html'
