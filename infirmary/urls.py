from django.urls import path, include
from . import views

app_name='infirmary'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-patient', views.add, name='add'),
    path('pacient', views.pacient, name='pacient'),
]