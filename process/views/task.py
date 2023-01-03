from django.views.decorators.csrf import csrf_exempt
import process.tasks as tasks
from django.http import JsonResponse
from django.core.cache import cache

@csrf_exempt
def calculate(request):
    file_content = request.FILES['file'].read().decode("utf-8")
    data = []
    lines = file_content.split("\n")
    for line in lines:
        if line != "":
            line_data = line.split(",")
            line_data = [float(i) for i in line_data]
            data.append(line_data)
    task_ids = {
        'median': tasks.median.delay(data).id
    }
    cache.set('task_ids', task_ids)
    return JsonResponse(task_ids, safe=False)