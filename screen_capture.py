import pyautogui

def capture_screen(filename="screen.png"):
    """Capture the screen and save it to a file."""
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
