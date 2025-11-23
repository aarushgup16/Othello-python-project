# board.py
# Board representation and basic helpers

EMPTY = "."
BLACK = "B"
WHITE = "W"

# 8 directions to check around a square
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]


def create_board():
    """Create the initial 8x8 Othello board."""
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE
    return board


def inside(r, c):
    """Return True if (r, c) is inside the board."""
    return 0 <= r < 8 and 0 <= c < 8


def count_pieces(board):
    """Count black and white pieces on the board."""
    black = sum(row.count(BLACK) for row in board)
    white = sum(row.count(WHITE) for row in board)
    return black, white
