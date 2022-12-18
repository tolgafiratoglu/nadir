from django.views.decorators.csrf import csrf_exempt

import process.tasks as tasks

from django.http import HttpResponse
import json

import numpy as np

@csrf_exempt
def calculate(request):
    data = request.POST.get('data')
    rows = data.split(';')
    data_arr = []
    tasks.median.delay(data_arr)
    for row in rows:
        cols = row.split(',')
        cols = [float(item) for item in cols]
        data_arr.append(cols)
    response = {
        'median': tasks.median.delay(data_arr).id
    }
    return HttpResponse(json.dumps(response))