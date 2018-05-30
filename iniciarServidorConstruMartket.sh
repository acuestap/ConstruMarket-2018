#!/bin/bash
# Montaje automático al iniciar el PC
echo "Eliminando registros de logs para ver solo el de la ultima ejecucion del servidor worker"
if [ -f /home/ubuntu/201810-Grupo-6/servidor.out ];
then
rm /home/ubuntu/201810-Grupo-6/servidor.out
fi
if [ -f /home/ubuntu/201810-Grupo-6/servidor.err ];
then
rm /home/ubuntu/201810-Grupo-6/servidor.err
fi
if [ -f /home/ubuntu/201810-Grupo-6/ConstruMartket/celerybeat.pid ];
then
rm /home/ubuntu/201810-Grupo-6/ConstruMartket/celerybeat.pid
fi

#echo "Iniciando servidor ConstruMartket..."
cd /home/ubuntu/201810-Grupo-6/ConstruMartket/
#echo "Levantando servicio..."
python manage.py runserver 0.0.0.0:8000 > /home/ubuntu/201810-Grupo-6/servidor.err 2> /home/ubuntu/201810-Grupo-6/servidor.out < /dev/null &
#echo "Servidor ConstrutMarhet iniciado"
exit
