import time

from core.celery.celery import celery_app


@celery_app.task(acks_late=True)
def get_hello(item_id: int):
    time.sleep(0.5)
    s = 'Hello - ' + str(item_id)
    print(s)
    return s
