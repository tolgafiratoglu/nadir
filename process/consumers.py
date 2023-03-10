import json
from channels.generic.websocket import WebsocketConsumer
import threading
from django.core.cache import cache
from celery.result import AsyncResult

class ProcessConsumer(WebsocketConsumer):
    def publish_task_results(self):
        task_ids = cache.get('task_ids')
        results = {'SUCCESS': {}, 'PENDING': {}, 'STARTED': {}, 'RETRY': {}, 'FAILURE': {}}
        for scope,task_id in task_ids.items():
            result = AsyncResult(task_id)
            if result.status == 'SUCCESS':
                results[result.status][scope] = result.result
            elif result.status == 'FAILURE':
                results[result.status][scope] = 'Task Failed'
        self.send(text_data = json.dumps({
            'type': 'task_results',
            'results': results,
        }))
        threading.Timer(1.0, self.publish_task_results).start()

    def connect(self):
        self.accept()
        self.publish_task_results
        self.send(text_data = json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected',
        }))
        threading.Timer(1.0, self.publish_task_results).start()
        
