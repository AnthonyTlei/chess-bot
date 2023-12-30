import cv2
import numpy as np
import utils

templates = {
    'K': ['templates/white_king_1.png', 'templates/white_king_2.png'],
    'Q': ['templates/white_queen_1.png', 'templates/white_queen_2.png'],
    'R': ['templates/white_rook_1.png', 'templates/white_rook_2.png'],
    'B': ['templates/white_bishop_1.png', 'templates/white_bishop_2.png'],
    'N': ['templates/white_knight_1.png', 'templates/white_knight_2.png'],
    'P': ['templates/white_pawn_1.png', 'templates/white_pawn_2.png'],
    'k': ['templates/black_king_1.png', 'templates/black_king_2.png'],
    'q': ['templates/black_queen_1.png', 'templates/black_queen_2.png'],
    'r': ['templates/black_rook_1.png', 'templates/black_rook_2.png'],
    'b': ['templates/black_bishop_1.png', 'templates/black_bishop_2.png'],
    'n': ['templates/black_knight_1.png', 'templates/black_knight_2.png'],
    'p': ['templates/black_pawn_1.png', 'templates/black_pawn_2.png'],
}

# Load and resize the templates
loaded_templates = {}
for piece, paths in templates.items():
    loaded_templates[piece] = [cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), (100, 100)) for path in paths]

def validate_squares(squares):
    valid = True
    if len(squares) != 8:
        print("Failed to split board into squares.")
        valid = False
    for row in squares:
        if len(row) != 8:
            print("Failed to split board into squares.")
            valid = False
        for square in row:
            if square is None:
                print("Failed to split board into squares.")
                valid = False
            else:
                continue
    return valid

def validate_templates(templates):
    valid = True
    for piece, image in templates.items():
        if image is None:
            print(f"Failed to load template for {piece}.")
            valid = False
        else:
            continue
    return valid

def split_board_into_squares(board_image):
    squares = []
    size = board_image.shape[0] // 8
    for i in range(8):
        row = []
        for j in range(8):
            square = board_image[i*size:(i+1)*size, j*size:(j+1)*size]
            row.append(square)
        squares.append(row)
    return squares

def recognize_piece(square_image, templates):
    best_match = None
    highest_val = 0
    threshold = 0.55  # Adjust the threshold as necessary

    for piece_name, template_set in templates.items():
        for template in template_set:
            res = cv2.matchTemplate(square_image, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > highest_val:
                highest_val = max_val
                best_match = piece_name

    if highest_val > threshold:
        print(f"Recognized {best_match} with confidence {highest_val}")
        return best_match
    else:
        print("No piece recognized in this square.")
        return None
    
def board_to_fen(squares, templates):
    fen_rows = []
    for row in squares:
        fen_row = []
        empty_count = 0
        for square in row:
            piece = recognize_piece(square, templates)
            if piece:
                if empty_count > 0:
                    fen_row.append(str(empty_count))
                    empty_count = 0
                fen_row.append(piece)
            else:
                empty_count += 1
        if empty_count > 0:
            fen_row.append(str(empty_count))
        fen_rows.append(''.join(fen_row))
    fen = '/'.join(fen_rows) + ' w KQkq - 0 1'
    return fen

def extract_position(board_image_path):
    # Load the board image in grayscale
    board_image = cv2.imread(board_image_path, cv2.IMREAD_GRAYSCALE)

    # Split the board into squares
    squares = split_board_into_squares(board_image)

    # Validate squares
    if not validate_squares(squares):
        print("Error splitting board into squares. Please check the board image.")
    else:
        print("Board split into squares successfully.")
        
    # Validate templates
    if not validate_templates(loaded_templates):
        print("Error loading some templates. Please check the template files.")
    else:
        print("All templates loaded successfully.")

    fen = board_to_fen(squares, loaded_templates)
    return fen