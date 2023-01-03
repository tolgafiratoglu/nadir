import random
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {
        'randint': random.randrange(1, 1000),
    })