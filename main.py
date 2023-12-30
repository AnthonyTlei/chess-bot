import keyboard
import screen_capture
import chessboard_detector
import chess_position_extractor
import chessboard_visualizer
import utils
import webbrowser

def on_hotkey():
    print("Hotkey pressed, capturing screen...")
    # Capture the screen
    screen_capture.capture_screen("screen.png")

    # Detect and correct the chessboard
    chessboard_image = chessboard_detector.detect_chessboard("screen.png")

    # Save chessboard image as board.png
    utils.write_image(chessboard_image, "board.png")

    # Display the chessboard
    # utils.display_image(chessboard_image, title="Chessboard")

    # Extract the chess position
    if chessboard_image is not None:
        fen = chess_position_extractor.extract_position("board.png")
        print(f"Extracted FEN: {fen}")
    else:
        print("Chessboard could not be detected.")

    # Draw the chessboard
    chessboard_visualizer.draw_chessboard(fen, save_path='board.svg')
    webbrowser.open('board.svg')

# Register the hotkey and associate it with the on_hotkey() function
keyboard.add_hotkey('shift+alt+5', on_hotkey)

print("Script is running in the background...")

# Keep the script running in the background
keyboard.wait()
