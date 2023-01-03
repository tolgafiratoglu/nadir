from celery import shared_task
import numpy as np

@shared_task
def ptp(arr, axis=0):
    return np.ptp(arr, axis).tolist()

@shared_task
def percentile(arr, percentile=50, axis=0):
    return np.percentile(arr, percentile, axis).tolist()

@shared_task
def nanpercentile(arr, percentile=50, axis=0):
    return np.nanpercentile(arr, percentile, axis).tolist()

@shared_task
def quantile(arr, percentile=50, axis=0):
    return np.quantile(arr, percentile, axis).tolist()

@shared_task
def nanquantile(arr, percentile=50, axis=0):
    return np.nanquantile(arr, percentile, axis).tolist()

@shared_task
def median(arr, axis=0):
    return np.median(arr, axis).tolist()    

@shared_task
def average(arr, axis=0):
    return np.average(arr, axis).tolist()

@shared_task
def mean(arr, axis=0):
    return np.mean(arr, axis).tolist()    

@shared_task
def std(arr, axis=0):
    return np.std(arr, axis).tolist()    

@shared_task
def var(arr, axis=0):
    return np.var(arr, axis).tolist()

@shared_task
def nanmedian(arr, axis=0):
    return np.nanmedian(arr, axis).tolist()

@shared_task
def nanmean(arr, axis=0):
    return np.nanmean(arr, axis).tolist()