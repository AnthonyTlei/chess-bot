import cv2
import numpy as np
import keyboard
import screen_capture
import chessboard_detector

# This function will be triggered when the hotkey is pressed
def on_hotkey():
    print("Hotkey pressed, capturing screen...")
    # Capture the screen
    screen_capture.capture_screen("screen.png")

    # Detect and correct the chessboard
    board = chessboard_detector.detect_chessboard("screen.png")

    # Show the corrected chessboard
    cv2.imshow('Chessboard', board)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Register the hotkey and associate it with the on_hotkey() function
keyboard.add_hotkey('shift+alt+5', on_hotkey)

print("Script is running in the background...")

# Keep the script running in the background
keyboard.wait()
