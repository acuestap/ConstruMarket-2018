from django.conf.urls import url


from usuario.views import RegistroUsuariosMasivo, RegistroUsuarioBasico, RegistroUsuario, RegistroUsuarioSimple, index

urlpatterns = [
    url(r'^registroMasivo', RegistroUsuariosMasivo.as_view(), name='registroMasivo'),
    url(r'^registroBasico', RegistroUsuarioBasico.as_view(), name='registroBasico'),
    url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),
    url(r'^registroSimple', RegistroUsuarioSimple.as_view(), name='registroSimple'),
    url(r'^',  index, name='inicio_usuario')
]
