from teacher.models import Teacher
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def TeacherList(request: HttpRequest):
    teachers = Teacher.objects.all()
    context = {"teachers": teachers}
    template = "teacher-list.html"
    return render(request, template, context)

@require_http_methods(['GET'])
def TeacherDetail(request, teacher_id):
    if Teacher.objects.filter(pk=teacher_id).exists():
        context = {'teacher': Teacher.objects.get(pk=teacher_id)}
        template = "teacher-detail.html"
        return render(request, template, context)
    else:
        return render(request, '404.html')
