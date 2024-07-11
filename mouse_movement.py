import pyautogui
import time
import numpy as np
from utils import random_walk, gaussian_smooth, morph_distribution

def simulate_mouse_movement():
    length = 100
    stddev = 10
    random_x = random_walk(length, stddev)
    random_y = random_walk(length, stddev)

    smooth_x = gaussian_smooth(random_x, sigma=2)
    smooth_y = gaussian_smooth(random_y, sigma=2)

    human_mean_x, human_std_x = 5, 2
    human_mean_y, human_std_y = 5, 2
    morphed_x = morph_distribution(smooth_x, human_mean_x, human_std_x)
    morphed_y = morph_distribution(smooth_y, human_mean_y, human_std_y)

    mouse_path = list(zip(morphed_x, morphed_y))

    for x, y in mouse_path:
        move_mouse_to(x, y)
        time.sleep(np.random.uniform(1, 2))

def move_mouse_to(x, y):
    try:
        pyautogui.moveTo(x, y)
    except Exception as e:
        print(f"Error moving mouse to ({x}, {y}): {e}")
