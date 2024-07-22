from django.urls import path
from .views import *

urlpatterns = [
    # path('',StudentAPI.as_view()),
    path('',index),
    path('Crud_opt/',Crud_opt.as_view()),
    path('Crud_opt/<int:pk>/',Crud_opt2.as_view()),
    # path('Productmng/',Productmng1.as_view()),
    # path('Productmng/<int:pk>/',Productmng.as_view()),
]
