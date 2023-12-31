import chess
import chess.engine

def get_best_move(fen, engine_path):
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        board = chess.Board(fen)
        print("Turn:", "White" if board.turn == chess.WHITE else "Black")
        print(f"\n{board}")
        # result = engine.play(board, chess.engine.Limit(time=2.0))  # Set time limit
        result = engine.play(board, chess.engine.Limit(depth=25))  # Set depth limit
        return result.move
