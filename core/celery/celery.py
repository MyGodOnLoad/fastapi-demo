from celery import Celery

from core import settings

CELERY_NAME = settings.app_settings.CELERY_NAME
celery_app = Celery(CELERY_NAME, include=['tasks'])
celery_app.config_from_object('core.celery.celeryconfig')
# celery_app.autodiscover_tasks(['celery_server.tasks'])
