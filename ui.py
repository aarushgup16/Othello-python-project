# ui.py
# User interface / I/O functions and game loop

from board import BLACK, WHITE, create_board, inside, count_pieces
from game_logic import valid_moves, make_move


def print_board(board, moves=None):
    """Print the board. Mark valid moves with '*' if provided."""
    print("  a b c d e f g h")
    for r in range(8):
        print(r + 1, end=" ")
        for c in range(8):
            if moves and (r, c) in moves:
                print("*", end=" ")
            else:
                print(board[r][c], end=" ")
        print()
    print()


def move_to_string(r, c):
    col_letter = chr(ord('a') + c)
    row_number = r + 1
    return f"{col_letter}{row_number}"


def format_moves_naturally(moves_str):
    """Format a list like ['d3','c4','f6'] into 'c4, d3 and f6'."""
    moves_str = sorted(moves_str)

    if len(moves_str) == 0:
        return ""
    if len(moves_str) == 1:
        return moves_str[0]
    if len(moves_str) == 2:
        return f"{moves_str[0]} and {moves_str[1]}"
    return ", ".join(moves_str[:-1]) + " and " + moves_str[-1]


def parse_move(move):
    """Convert user input like 'd3' into (row, col) or None if invalid."""
    move = move.strip().lower()
    if len(move) != 2:
        return None
    if not move[0].isalpha() or not move[1].isdigit():
        return None

    col = ord(move[0]) - ord('a')
    row = int(move[1]) - 1

    if inside(row, col):
        return (row, col)
    return None


def run_game():
    """Main game loop handling turns and user interaction."""
    board = create_board()
    current_player = BLACK

    while True:
        moves = valid_moves(board, current_player)
        print_board(board, moves)

        if not moves:
            opponent = WHITE if current_player == BLACK else BLACK
            if not valid_moves(board, opponent):
                print("No moves for both players. Game Over!")
                break
            print(f"No valid moves for {current_player}. Skipping turn.")
            current_player = opponent
            continue

        moves_str = [move_to_string(r, c) for (r, c) in moves]
        natural = format_moves_naturally(moves_str)

        print(f"Player {current_player}'s turn.")
        print(f"Possible moves are {natural}.")

        move = input("Enter your move (e.g., d3): ")
        parsed = parse_move(move)

        if not parsed:
            print("Invalid input.")
            continue

        r, c = parsed
        if (r, c) not in moves:
            print("Not a valid move.")
            continue

        make_move(board, r, c, current_player)
        current_player = WHITE if current_player == BLACK else BLACK

    # Game over - count and display result
    black, white = count_pieces(board)
    print_board(board)
    print(f"Final Count → Black: {black}, White: {white}")

    if black > white:
        print("Black wins!")
    elif white > black:
        print("White wins!")
    else:
        print("It's a tie!")
