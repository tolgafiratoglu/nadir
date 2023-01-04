Nadir is a practice project, an open source tool to analyse a large CSV file with statistical functions using Django, Celery, Numpy and websocket together. Celery process numpy functions parallel to each other. Websocket connection check celery task results to the main panel.

<h6>Installation</h6>
We strongly suggest to have a virtual environment:

<code>source venv/bin/activate</code>

You can install requirements:

<code>pip install -r requirements.txt</code>

This will install celery as well as other components like Django. 

<h6>Configuring Redis and RabbitMQ</h6>
Celery workers use Redis and RabbitMQ. Broker url is the RabbitMQ configuration. Please change this value to yours if it's different. Result backend is the redis connection. 

<code>
CELERY_BROKER_URL='amqp://root:root@localhost/celeryvhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
</code>

<h6>Running Celery and Django Server</h6>

As the third step, you need to start 2 services in the project folder:

<code>celery -A nadir worker --loglevel=INFO</code>

Open a new terminal tab, and run the following command in the project folder:

<code>python3 manage.py runserver</code>

Congrats! Now you can play and practice with the project. 