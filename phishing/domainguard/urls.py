from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("URLs/", views.URLs,name="urls"),
    path("result/",views.result,name="result")
]