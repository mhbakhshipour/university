from teacher.models import Teacher
from blog.models import Blog
from core.models import File
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def Index(request: HttpRequest):
    blogs = Blog.objects.filter(is_public=True)[:4]
    teachers = Teacher.objects.all()[:4]
    context = {
        "blogs": blogs,
        "teachers": teachers
        }
    template = "index.html"
    return render(request, template, context)

@require_http_methods(["GET"])
def Form(request: HttpRequest):
    forms = File.objects.all()
    context = {"forms": forms}
    template = "forms.html"
    return render(request, template, context)
