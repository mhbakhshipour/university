from django.urls import path

from core import views

coreview_urlpatterns = [
    path('', views.Index, name="index"),
    path('form', views.Form, name="form"),
]
