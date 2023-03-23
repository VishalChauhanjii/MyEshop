from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.views import View


def Store(request):
    return render(request, "store.html")
