from django.views.decorators.csrf import csrf_exempt
import process.tasks as tasks
from django.http import HttpResponse, JsonResponse
import json
import numpy as np

import csv
import io

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
    response = {
        'median': tasks.median.delay(data).id
    }
    return JsonResponse(response, safe=False)