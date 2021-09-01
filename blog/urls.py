from django.urls import path

from blog import views

blogview_urlpatterns = [
    path('list', views.BlogList, name="list"),
    # path('<int:blog_id>', views.BlogDetail, name="detail"),
]
