
import chessboard_analyzer
import chessboard_detector
import chessboard_parser
import chessboard_preparer
import chessboard_visualizer
from dotenv import load_dotenv
import keyboard
import os
import screen_capture
import utils
import webbrowser

# Load the environment variables from .env file
load_dotenv()

# Retrieve the engine path
engine_path = os.getenv('STOCKFISH_ENGINE_PATH')
tesseract_path = os.getenv('TESSERACT_PATH')

def on_hotkey():
    print("Hotkey pressed, capturing screen...")
    # Capture the screen
    screen_capture.capture_screen("screen.png")

    # Detect and correct the chessboard
    chessboard_image = chessboard_detector.detect_chessboard("screen.png")

    # Save chessboard image as board.png
    utils.write_image(chessboard_image, "board.png")

    # Display the chessboard
    utils.display_image(chessboard_image, title="Chessboard")

    # Prepare board
    if chessboard_image is not None:
        prepared_board, is_flipped_board = chessboard_preparer.prepare_board("board.png")
    else:
        print("Chessboard could not be detected.")

    # Extract the chess position
    if prepared_board is not None:
        fen = chessboard_parser.extract_position(prepared_board, is_flipped_board)
        print(f"Extracted FEN: {fen}")
    else:
        print("Chessboard could not be detected.")

    # Draw & Display the chessboard
    if fen is not None:
        chessboard_visualizer.draw_chessboard(fen, save_path='board.svg')
        webbrowser.open('board.svg')
    else:
        print("Chess position could not be extracted.")

    # Get the best move
    if fen is not None:
        board, turn, best_move = chessboard_analyzer.get_best_move(fen, engine_path)
        print(f"\n{board}\n")
        print(f"Turn: {turn}\n")
        print(f"\nBest move: {best_move}\n\n")
    else:
        print("Chess position could not be extracted.")

# Register the hotkey and associate it with the on_hotkey() function
keyboard.add_hotkey('shift+alt+5', on_hotkey)

print("Script is running in the background...")

# Keep the script running in the background
keyboard.wait()
