"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import class_, func_
from task4.views import shop, basket
from task5.views import sign_up_by_django, sign_up_by_html, sign_up_url
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', class_.as_view()),
    path('func/', func_),
    path('', TemplateView.as_view(template_name='fourth_task/start_template.html')),
    path('shop/', shop),
    path('basket/', basket),
    path('django_sign_up/', sign_up_by_django),
    path('register/', sign_up_by_html),
    path('reg/', sign_up_url),
]
