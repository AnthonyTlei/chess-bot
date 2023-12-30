import screen_capture
import chessboard_detector

def main():
    # Capture the screen
    screen_capture.capture_screen("screen.png")

    # Detect the chessboard
    chessboard_detector.detect_chessboard("screen.png")

if __name__ == "__main__":
    main()
