from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("home/",views.index),
    path("contact/",views.contact),
    path("gallery/",views.gallery),
    path("wchoose/",views.wchoose),
    path("team/",views.team),
    path("booking/",views.mybooking),
    path("foodmenu/",views.foodmenu),
    path("services/",views.services),

]

