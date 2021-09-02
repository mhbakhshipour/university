from blog.models import Blog
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def BlogList(request: HttpRequest):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    template = "blog-list.html"
    return render(request, template, context)
