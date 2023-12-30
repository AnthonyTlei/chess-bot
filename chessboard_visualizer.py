import chess
import chess.svg

def draw_chessboard(fen, save_path='chessboard.svg'):
    board = chess.Board(fen)
    svg = chess.svg.board(board=board)
    with open(save_path, 'w') as f:
        f.write(svg)
