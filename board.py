EMPTY = "○"
BLACK = "B"
WHITE = "W"

# 8 directions to check around a square
DIRECTIONS = [(-1, -1),(-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]


def create_board():
    #creating the board for the game
    board = []
    for i in range(8):
        row = [EMPTY for i in range(8)]
        board.append(row)
    board[3][3] = WHITE 
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE
    return board


def inside(r, c):
    #chekcing if the moves are valid or not
    if r < 0 or c < 0:
        return False
    if r >= 8 or c >= 8:
        return False
    
    return True


def count_pieces(board):
    #this func counts the number of black and white pieces on the board
    black_count = 0
    white_count = 0
    for row in board:
        black_count += row.count(BLACK)
        white_count += row.count(WHITE)
    return black_count, white_count
    
