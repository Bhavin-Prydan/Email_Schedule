import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# from django.apps import apps


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_schedule.settings')

app = Celery('email_schedule')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)
# app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
# app.autodiscover_tasks(
#     lambda: settings.INSTALLED_APPS + settings.INSTALLED_APPS_WITH_APPCONFIGS
# )


app.conf.beat_schedule = {
    'send-every-1min' :{
        'task' : 'send_Reminder',
        'schedule' : crontab(minute='*/1')

    }
}

# @app.task(bind=True)
# def debug_task(self):
#     print('Hello Celery !@#')

@app.task()
def print_hello():
    print('Hello Goku !@#')



# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


# for run celery 
    # celery -A email_schedule worker -l INFO

# for run celery beat
    # celery -A email_schedule beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
           
