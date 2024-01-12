from django.urls import path,include
from . import views

from django.contrib import admin


urlpatterns = [
    path('', views.predictor, name='predictor'),
    path('result', views.formInfo, name='result'),
]
