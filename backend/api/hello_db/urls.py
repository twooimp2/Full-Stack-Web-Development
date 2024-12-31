from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('backend/', views.Db.as_view())
]