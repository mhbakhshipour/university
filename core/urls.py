from django.urls import path

from core import views

coreview_urlpatterns = [
    path('', views.Index, name="index"),
    # path('<int:teacher_id>', views.TeacherDetail, name="detail"),
]
