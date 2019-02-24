from django.urls import path

from . import views

app_name = 'skurcz_to'

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten_long_url, name='shorten_url'),
    path('<str:code>/', views.obtain_long_url, name='get_url'),
]
