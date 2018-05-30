# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Orden, Detalle_pago, Detalle_orden
'''

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from orden.tasks import buscar_detalle_pago
'''
# Create your views here.

def detalles_pago_buscar(request):
    try:
        #Se registra el log en archivo.
        logger.debug('>>> Inicio busqueda de ordenes de pago.')

        continuar = False

        page = "1"

        mensaje = "Cliente: --> Valor: --> Page:" + page

        if request.POST:
            continuar = True

        if continuar == False:
            lista_detalle_pagos = Detalle_pago.objects.order_by('-fecha_pago')
        else:
            nombre_cliente = request.POST.get('nombre_cliente')
            valor = request.POST.get('valor')

            if str(valor) == "":
                valor = "0"

            mensaje = "Cliente:" + nombre_cliente + "--> Valor:" + str(valor) + "--> Page:" + page

            querys = (Q(id_orden__id_cliente__primer_nombre__contains=nombre_cliente)
                      | Q(id_orden__id_cliente__segundo_nombre__contains=nombre_cliente))
            querys |= Q(id_orden__detalle_pago__valor_total__in=[int(valor)])

            lista_detalle_pagos = Detalle_pago.objects.filter(querys)

        if lista_detalle_pagos.count() > 0:
            paginator = Paginator(lista_detalle_pagos, 25)  # Muestra 25 registros por pagina

            if request.GET:
                page = request.GET.get('page')

            if str(page) == "None":
                page = "1"

            lista_detalle_pagos = paginator.page(int(page))

        context = {'lista_detalle_pagos': lista_detalle_pagos}

        #Se registra el log en archivo.
        logger.debug('>>> FIN busqueda de ordenes de pago: {}.'.format(mensaje))

    except Exception as e:
        #Se registra el log en archivo.
        logger.error('Detalle: {}'.format(e))
        lista_detalle_pagos = Detalle_pago.objects.order_by('-fecha_pago')
        context = {'lista_detalle_pagos': lista_detalle_pagos}

    return render(request, 'orden/listar.html', context)

'''
# Pruebas para incluir mediante proceso de colas.

def abrir_pagina(request):
    return HttpResponse("Cargando...")
    # return render_template("orden/listar.html")


def detalles_pago_buscar(request):
    continuar = False
    nombre_cliente = ""
    valor = ""
    page = "1"

    if request.POST:
        continuar = True


    if request.GET:
        page = request.GET.get('page')


    if continuar == True:
        nombre_cliente = request.POST.get('nombre_cliente')
        valor = request.POST.get('valor')

    # Se adiciona la solicitud a la cola de mensajes
    # buscar_detalle_pago.delay(nombre_cliente, valor, page, continuar)

    # lista_detalle_pago = buscar_detalle_pago.delay(nombre_cliente, valor, page, continuar)

    # context = {'lista_detalle_pagos': lista_detalle_pago}

    # return HttpResponse(context)
    # return render(request, 'orden/listar.html')

    # return redirect('abrir_pagina')
    # return render_template("orden/listar.html")

'''