import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading
import keyboard
import numpy as np
from mouse_movement import simulate_mouse_movement, move_mouse_to
from mouse_click import click_mouse
from random_typing import type_random_text
from keyboard_monitor import start_keyboard_monitoring, stop_automation

class MouseAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Automation App")
        
        self.coordinates = []

        self.coord_label = tk.Label(root, text="Coordinates:")
        self.coord_label.pack()

        self.coord_listbox = tk.Listbox(root)
        self.coord_listbox.pack()

        self.record_button = tk.Button(root, text="Start Recording Coordinates (press 'q')", command=self.start_recording)
        self.record_button.pack()

        self.start_button = tk.Button(root, text="Start Automation", command=self.start_automation)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Automation (press 'esc')", command=self.stop_automation)
        self.stop_button.pack()

    def start_recording(self):
        self.recording_thread = threading.Thread(target=self.record_coordinates)
        self.recording_thread.start()

    def record_coordinates(self):
        while True:
            if keyboard.is_pressed('q'):
                x, y = pyautogui.position()
                self.coordinates.append((x, y))
                self.coord_listbox.insert(tk.END, f"({x}, {y})")
                time.sleep(0.5)  # Small delay to avoid multiple detections
            elif keyboard.is_pressed('0'):
                break

    def start_automation(self):
        if not self.coordinates:
            messagebox.showwarning("No Coordinates", "No coordinates recorded. Please record some coordinates first.")
            return
        
        self.keyboard_thread = start_keyboard_monitoring()
        self.run_automation()

    def run_automation(self):
        global stop_automation
        stop_automation = False
        count = 0

        while count < 30 and not stop_automation:
            for x, y in self.coordinates:
                if stop_automation:
                    break
                simulate_mouse_movement()
                move_mouse_to(x, y)
                click_mouse()
                type_random_text()
                time.sleep(np.random.uniform(2, 4))
            count += 1
        
        if not stop_automation:
            messagebox.showinfo("Automation Complete", "Automation process completed.")
        
    def stop_automation(self):
        global stop_automation
        stop_automation = True
        self.keyboard_thread.join()

def main():
    root = tk.Tk()
    app = MouseAutomationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
