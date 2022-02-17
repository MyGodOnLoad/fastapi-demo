celery -A celery_server.tasks.test_tasks worker -l info -Q test_tasks

flower -A celery_tasks --broker=amqp://guest:guest@192.168.3.14:5672 --address=0.0.0.0 --port=5550
