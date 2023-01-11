Nadir is a practice project, an open source tool to analyse large CSV files with statistical functions using Django, Celery, Numpy and websocket together. Celery process numpy functions parallel to each other. Websocket connection check celery task results and feed the main panel. 

This practice project aims to be educational for the power of Celery and teach new beginners about working with advanced Django topics.

<h6>Installation</h6>
Here're the steps you will need to take after cloning the project to your local directory. We strongly recommend you to have a virtual environment:

```
source venv/bin/activate
```

You can install requirements:

```
pip install -r requirements.txt
```

This will install celery as well as other components like Django. 

<h6>Configuring Redis and RabbitMQ</h6>
Celery workers use Redis and RabbitMQ. Broker url is the RabbitMQ configuration. Please change this value to yours if it's different. Result backend is the redis connection. 

```
CELERY_BROKER_URL='amqp://root:root@localhost/celeryvhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
```

<h6>Running Celery and Django Server</h6>

As the third step, you need to start 2 services in the project folder:

```
celery -A nadir worker --loglevel=INFO
```

Open a new terminal tab, and run the following command in the project folder:

```
python3 manage.py runserver
```

<h6>Working with Redis</h6>
If Redis is not up and running, you may need to start redis server. 

```
redis-server
```

If you want to see task keys in Redis:

```
redis-cli
keys *
```

You see the keys related with Celery. If you get one of them, you can see the result of the task. 

Congrats! Now you can play and practice with the project. 
