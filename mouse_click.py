import pyautogui

def click_mouse():
    try:
        pyautogui.click()
    except Exception as e:
        print(f"Error clicking mouse: {e}")
