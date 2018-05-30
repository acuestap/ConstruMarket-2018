from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construMartket.settings')

from django.conf import settings  # noqa

app = Celery('CeleryApp')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    # BROKER_URL = 'django://',
    BROKER_URL = 'redis://localhost:6379',
    # CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
)

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml'],

)