# Setup

1. Install dependencies
   pip install -r requirements.txt

2. Download and add engine path to .env
   e.g. STOCKFISH_ENGINE_PATH="path-to/stockfish/stockfish.exe"

3. Download and add Tesseract OCR path to .env
   e.g. TESSERACT_PATH="path-to/tesseract/tesseract.exe"

4. Run the script
   python main.py

5. Make sure a chessboard is visible on screen (Preferrably chess.com Standard theme) then press the shortcut
   shift+alt+5

# Features

- Detect and extract Chessboard on screen

- Parse Chessboard into FEN

- Generate a Chessboard from FEN

- Find best move in a position

- Handles flipped boards

# Demo

![Puzzle Example](/demo/puzzle.png)

![Extracted Position](/demo/extracted.png)

![Output](/demo/output.png)

# Disclaimer

This software is developed for educational and studying purposes only. It's intended to help understand and analyze chess games for learning. Users are advised not to use this software for cheating in online or competitive chess environments. Misuse of this software for cheating violates the fair play policies of most chess platforms and can result in bans or other penalties.
