# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from django.contrib import messages
from django.views.generic.edit import FormView


from usuario.forms import FormularioUsuariosMasivo, FormularioUsuarioBasico, RegistroForm
from usuario.tasks import crear_usuarios_masivo, crear_usuario_basico
import string
from celery.result import AsyncResult

class RegistroUsuariosMasivo(FormView):
    template_name = "usuario/registroMasivo.html"
    form_class = FormularioUsuariosMasivo

    def form_valid(self, form):
        try:
            total = form.cleaned_data.get('total')
            crear_usuarios_masivo.delay(total)
            messages.success(self.request, '>>> Se han creando los ( {} ) usuarios!'.format(total))
            return redirect('registroMasivo')
        except Exception as e:
           #Se registra el log en archivo.
           logger.error('Detalle: {}'.format(e))


class RegistroUsuarioBasico(FormView):
    template_name = "usuario/registroBasico.html"
    form_class = FormularioUsuarioBasico

    def form_valid(self, form):
        try:
            usuario = form.cleaned_data.get('username')

            #Se envia la tarea a la cola.
            tarea = crear_usuario_basico.delay(usuario)
            work = crear_usuario_basico.AsyncResult(tarea.id)

            if(work.state == 'PENDING'):
                if User.objects.filter(username=usuario).count():
                    resultado = '>>> El usuario ({}) ya existe!'.format(usuario)
                else:
                    resultado = '>>> El usuario ({}) se ha creado correctamente!'.format(usuario)
            else:
                resultado = work.result

            mensaje =  '{}'.format(resultado)
            messages.success(self.request, mensaje)
            return redirect('registroBasico')
        except Exception as e:
           #Se registra el log en archivo.
           logger.error('Detalle: {}'.format(e))


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm #UserCreationForm
    success_url = reverse_lazy('inicio')


class RegistroUsuarioSimple(CreateView):
    model = User
    template_name = "usuario/registroSimple.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('inicio')

def index(request):
    # resultado = prueba_suma.delay(30,6)

    # return HttpResponse("Hola Celery n")
    return render(request, 'usuario/index.html')

