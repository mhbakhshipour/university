from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def Index(request: HttpRequest):
    context = {"title": "Index"}
    template = "index.html"
    return render(request, template, context)
