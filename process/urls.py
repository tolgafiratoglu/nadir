from django.urls import path

from process.views.task import calculate

urlpatterns = [
    path('calculate', calculate, name='calculate')
]