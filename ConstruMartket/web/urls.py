from django.conf.urls import url

from web import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^', login_required(views.index), name='inicio'),

]
