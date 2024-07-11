import numpy as np
from scipy.ndimage import gaussian_filter1d

def random_walk(length, stddev):
    return np.cumsum(np.random.normal(0, stddev, length))

def gaussian_smooth(data, sigma):
    return gaussian_filter1d(data, sigma)

def morph_distribution(data, target_mean, target_std):
    return (data - np.mean(data)) / np.std(data) * target_std + target_mean
