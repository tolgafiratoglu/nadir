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
            results[result.status][scope] = result.result
        self.send(text_data = json.dumps({
            'type': 'task_result',
            'result': results,
        }))
        if len(results['SUCCESS'] < len(task_ids)):
            threading.Timer(1.0, self.publish_task_results).start()

    def connect(self):
        self.accept()
        self.publish_task_results
        self.send(text_data = json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected',
        }))
        threading.Timer(1.0, self.publish_task_results).start()
        
