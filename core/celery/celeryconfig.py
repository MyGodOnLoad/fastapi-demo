from kombu import Queue

from core import settings

RABBITMQ_USER = settings.app_settings.RABBITMQ_USER
RABBITMQ_PASSWORD = settings.app_settings.RABBITMQ_PASSWORD
RABBITMQ_SERVER = settings.app_settings.RABBITMQ_SERVER
RABBITMQ_PORT = settings.app_settings.RABBITMQ_PORT

broker_url = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_SERVER}:{RABBITMQ_PORT}'
result_backend = f'rpc://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_SERVER}:{RABBITMQ_PORT}'
task_track_started = True
result_serializer = "json"
accept_content = ['json']
timezone = "Asia/Shanghai"
enable_utc = True
result_expires = 60 * 60 * 24

# CELERY_QUEUES = (  # 设置add队列,绑定routing_key
#     Queue('default', routing_key='default'),
#     Queue('email', routing_key='send_email'),
# )
#
# CELERY_ROUTES = {
#     'app.api.api_v1.tasks.emails.decoratorEmail': {
#         'queue': 'email',
#         'routing_key': 'send_email',
#     }
# }
