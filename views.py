from django.http import HttpResponse
from django.shortcuts import render
from .models import Articles


def index(request):
    articles = Articles.objects.all()
    return render(request, "index.html",
                  {'articles': articles})


def new(request):
    return HttpResponse('new article')