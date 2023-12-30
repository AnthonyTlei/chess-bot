
import chessboard_detector
import chessboard_visualizer
from dotenv import load_dotenv
import position_analyzer
import keyboard
import os
import position_extractor
import screen_capture
import utils
import webbrowser

# Load the environment variables from .env file
load_dotenv()

# Retrieve the engine path
engine_path = os.getenv('STOCKFISH_ENGINE_PATH')

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
        fen = position_extractor.extract_position("board.png")
        print(f"Extracted FEN: {fen}")
    else:
        print("Chessboard could not be detected.")

    # Draw the chessboard
    chessboard_visualizer.draw_chessboard(fen, save_path='board.svg')
    # webbrowser.open('board.svg')

    # Get the best move
    best_move = position_analyzer.get_best_move(fen, engine_path)
    print(f"\nBest move: {best_move}\n\n")

# Register the hotkey and associate it with the on_hotkey() function
keyboard.add_hotkey('shift+alt+5', on_hotkey)

print("Script is running in the background...")

# Keep the script running in the background
keyboard.wait()
