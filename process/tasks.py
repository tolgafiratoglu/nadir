from celery import shared_task

import numpy as np

@shared_task
def median(arr, axis=0):
    return np.median(arr, axis).tolist()