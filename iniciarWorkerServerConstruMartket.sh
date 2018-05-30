#!/bin/bash
if [ -f /home/ubuntu/201810-Grupo-6/ConstruMartket/celerybeat.pid ];
then
echo "Ya existe un proceso ejecutandose..."
else
echo "Eliminando registros de logs para ver solo el de la ultima ejecucion del servidor worker"
if [ -f /home/ubuntu/201810-Grupo-6/tareas.out ];
then
rm /home/ubuntu/201810-Grupo-6/tareas.out
fi
if [ -f /home/ubuntu/201810-Grupo-6/tareas.err ];
then
rm /home/ubuntu/201810-Grupo-6/tareas.err
fi
if [ -f /home/ubuntu/201810-Grupo-6/supervisor.out ];
then
rm /home/ubuntu/201810-Grupo-6/supervisor.out
fi
if [ -f /home/ubuntu/201810-Grupo-6/supervisor.err ];
then
rm /home/ubuntu/201810-Grupo-6/supervisor.err
fi
echo "Iniciando daemon de tareas celery ..."
cd /home/ubuntu/201810-Grupo-6/ConstruMartket/
celery -A construMartket worker -l info --pool=solo > /home/ubuntu/201810-Grupo-6/tareas.err 2> /home/ubuntu/201810-Grupo-6/tareas.out < /dev/null &
echo "Tareas de celery iniciadas."
echo "Iniciando daemon del supervisor de celery ..."
celery -A construMartket beat -l info > /home/ubuntu/201810-Grupo-6/supervisor.err 2> /home/ubuntu/201810-Grupo-6/supervisor.out < /dev/null &
echo "Supervisor de celery iniciado."
echo "Worker iniciado."
fi
exit
