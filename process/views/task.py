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
        # Order Statistics:
        'ptp': tasks.ptp.delay(data).id,
        'percentile_per_25': tasks.percentile.delay(data, 25).id,
        'percentile_per_50': tasks.percentile.delay(data, 50).id,
        'percentile_per_75': tasks.percentile.delay(data, 75).id,
        'nanpercentile_per_50': tasks.nanpercentile.delay(data, 50).id,
        # Averages:
        'median': tasks.median.delay(data).id,
        'average': tasks.average.delay(data).id,
        'mean': tasks.mean.delay(data).id,
        'standard_deviation': tasks.std.delay(data).id,
        'variance': tasks.var.delay(data).id,
        'nanmedian': tasks.nanmedian.delay(data).id,
        'nanmean': tasks.nanmean.delay(data).id,
    }
    cache.set('task_ids', task_ids)
    return JsonResponse(task_ids, safe=False)