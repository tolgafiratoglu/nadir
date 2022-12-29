from django.urls import path

from process.views.task import calculate
from process.views.home import home

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('calculate', calculate, name='calculate'),
    path('', home, name='index'),
] + static(settings.STATIC_URL)