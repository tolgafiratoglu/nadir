from celery import shared_task

import numpy as np

@shared_task
def median(arr):
    return np.mean(arr)
