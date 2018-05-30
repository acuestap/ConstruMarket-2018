from django.conf.urls import url

from orden import views
# from orden.views import index, listar, detail
from django.contrib.auth.decorators import login_required

# ex: /orden/5/
urlpatterns = [
    url(r'^', login_required(views.detalles_pago_buscar), name='detalles_pago_buscar'),
    #url(r'^(?P<nombre_cliente>[(\w+) (\w+)]+)/', views.detalles_pago_buscar, name='detalles_pago_buscar'),
    #url(r'^detalle/(?P<id_orden>[0-9]+)/$', views.detail, name='detail'),
]