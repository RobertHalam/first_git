from django.contrib import admin
from django.urls import path,include
from classworkapp import views
from classworkapp.views import index

urlpatterns = [
    path('', views.index),
    path('redirect1', views.redirect1,name='home'),
    path('joker', views.joker),

    

]
