from django.urls import path

from . import views

app_name = 'skurcz_to'

urlpatterns = [
    path('', views.index, name='index'),
]
