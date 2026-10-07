# calc/stats.py
import math

def get_sum(values):
    result = 0.0
    for val in values:
        result += val
    return result

def get_mean(values):
    return get_sum(values) / len(values)

def get_sum_sq(values):
    result = 0.0
    for val in values:
        result += val ** 2
    return result

def get_rms(values):
    return math.sqrt(get_sum_sq(values) / len(values))

def get_variance_data(values):
    mean_val = get_mean(values)
    result = 0.0
    for val in values:
        result += (val - mean_val) ** 2
    return result

def get_variance(values):
    return get_variance_data(values) / len(values)

def get_std_dev_n(values):
    return math.sqrt(get_variance(values))

def get_std_dev_n1(values):
    if len(values) < 2:
        return None
    return math.sqrt(get_variance_data(values) / (len(values) - 1))

def get_min(values):
    result = values[0]
    for val in values:
        if val < result:
            result = val
    return result

def get_max(values):
    result = values[0]
    for val in values:
        if val > result:
            result = val
    return result

def get_positives(values):
    count = 0
    for val in values:
        if val > 0:
            count += 1
    return count

def get_negatives(values):
    count = 0
    for val in values:
        if val < 0:
            count += 1
    return count
