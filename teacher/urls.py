from django.urls import path

from teacher import views

teacherview_urlpatterns = [
    path('list', views.TeacherList, name="list"),
    path('<int:teacher_id>', views.TeacherDetail, name="detail"),
]
