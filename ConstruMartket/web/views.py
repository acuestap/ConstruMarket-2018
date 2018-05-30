# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from tasks import prueba_suma

# Create your views here.


def index(request):
    # resultado = prueba_suma.delay(30,6)

    # return HttpResponse("Hola Celery n")
    return render(request, 'web/inicio.html')

