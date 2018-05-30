import logging
logger = logging.getLogger(__name__)

from construMartket.celery import app
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

@app.task
def crear_usuarios_masivo(total):
    try:
        #Se registra el log en archivo.
        logger.debug('>>> Inicio creacion de los {} usuarios masivos'.format(total))

        for i in range(total):
            username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
            email = '{}@example.com'.format(username)
            password = get_random_string(50)

            User.objects.create_user(username=username, email=email, password=password)


        mensaje = '>>> Se han creado ( {} ) usuarios correctamente!'.format(total)

        #Se registra el log en archivo.
        logger.debug(mensaje)

        return mensaje
    except Exception as e:
        #Se registra el log en archivo.
        logger.error('Detalle: {}'.format(e))


@app.task
def crear_usuario_basico(username):
    try:
        #Se registra el log en archivo.
        logger.debug('>>> Inicio creacion de usuario basico: {}'.format(username))

        email = '{}@example.com'.format(username)
        password = get_random_string(50)

        User.objects.create_user(username=username, email=email, password=password)
        mensaje = '>>> El usuario ({}) se ha creado correctamente!'.format(username)

        #Se registra el log en archivo.
        logger.debug(mensaje)

        #return mensaje
    except Exception as e:
        #Se registra el log en archivo.
        #logger.error('XXX Error al intentar crear usuario basico', exc_info=True)
        mensaje = '>>> Se ha presentado un error durante el proceso: {}'.format(e)
        logger.error(mensaje)


    return mensaje



'''
try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            User.objects.create_user(username=username, email=email, password=password)
            return '{} random users created with success!'.format(total)
        raise
        return '{} random users created with fail!'.format(username)


def registration(request):
c= {}
c.update(csrf(request))
state = "Please Register below..."
username = None
email = None
password = None
user_success = None
user_created = None
if request.POST:
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print "username ",username

user = authenticate(username=username, password=password)
if user is not None:
    if user.is_active:
        user_created = True
    else:
        user_created = False
else:
        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        user.is_active = True
        user_success = True

return
'''