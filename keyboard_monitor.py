import threading
import keyboard
import time

stop_automation = False

def monitor_keyboard():
    global stop_automation
    while not stop_automation:
        if keyboard.is_pressed('esc'):
            stop_automation = True
            print("Escape key pressed. Stopping automation...")
            break
        time.sleep(0.1)
        
def start_keyboard_monitoring():
    keyboard_thread = threading.Thread(target=monitor_keyboard)
    keyboard_thread.start()
    return keyboard_thread
