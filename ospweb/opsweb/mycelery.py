import os
import django
from celery import Celery
from django.conf import settings
from celery import Celery,platforms
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycelery.settings')
platforms.C_FORCE_ROOT = True
django.setup()

app = Celery('tasks',backend='redis://:redis..123456@127.0.0.1:6379/0',broker='redis://:redis..123456@127.0.0.1:6379/1')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
