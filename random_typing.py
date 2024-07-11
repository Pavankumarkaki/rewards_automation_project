import pyautogui
import random
import string

def type_random_text():
    alphabet_string = string.ascii_lowercase + string.ascii_uppercase
    if random.choice([True, False]):
        text = random.choice(alphabet_string)
    else:
        words = ["hello", "world", "test", "python", "code"]
        text = random.choice(words)
    
    pyautogui.typewrite(text)
    pyautogui.press('enter')
