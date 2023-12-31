import cv2
from dotenv import load_dotenv
import os
import pytesseract
import utils

load_dotenv()
tesseract_path = os.getenv('TESSERACT_PATH')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def is_flipped(board, board_size=(824, 824)):
    square_size = board_size[0] // 8
    bottom_left_square_image = board[-square_size:, :square_size]
    resized_image = cv2.resize(bottom_left_square_image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    _, binary_image = cv2.threshold(resized_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    processed_image = cv2.resize(binary_image, (250, 250))
    height, width = processed_image.shape[:2]
    subsquare_fraction = 0.33
    subsquare_size = int(min(height, width) * subsquare_fraction)
    processed_image = processed_image[:subsquare_size, :subsquare_size]
    config = "--psm 10 --oem 3"
    bottom_left_square_text = pytesseract.image_to_string(processed_image, config=config)
    if "1" in bottom_left_square_text:
        return False
    else:
        return True
    
def prepare_board(board_path, board_size=(824, 824)):
    # Load the board image in grayscale
    prepared_board = cv2.imread(board_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the board image to a fixed size
    prepared_board = cv2.resize(prepared_board, board_size)
    is_flipped_board = is_flipped(prepared_board, board_size)

    return prepared_board, is_flipped_board