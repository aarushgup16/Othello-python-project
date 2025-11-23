# game_logic.py
# Core Othello rules and move logic

from board import EMPTY, BLACK, WHITE, DIRECTIONS, inside


def valid_moves(board, player):
    """Return a list of valid moves (r, c) for the given player."""
    opponent = WHITE if player == BLACK else BLACK
    valid = []

    for r in range(8):
        for c in range(8):
            if board[r][c] != EMPTY:
                continue

            for dr, dc in DIRECTIONS:
                rr, cc = r + dr, c + dc
                found_op = False

                # Move in direction while seeing opponent pieces
                while inside(rr, cc) and board[rr][cc] == opponent:
                    found_op = True
                    rr += dr
                    cc += dc

                # If we found opponent pieces and end on our own piece, it's valid
                if found_op and inside(rr, cc) and board[rr][cc] == player:
                    valid.append((r, c))
                    break

    return valid


def flip_pieces(board, r, c, player):
    """Flip opponent pieces affected by placing at (r, c)."""
    opponent = WHITE if player == BLACK else BLACK

    for dr, dc in DIRECTIONS:
        flips = []
        rr, cc = r + dr, c + dc

        while inside(rr, cc) and board[rr][cc] == opponent:
            flips.append((rr, cc))
            rr += dr
            cc += dc

        # Only flip if the sequence ends in our own piece
        if flips and inside(rr, cc) and board[rr][cc] == player:
            for x, y in flips:
                board[x][y] = player


def make_move(board, r, c, player):
    """Place a piece and flip the necessary opponent pieces."""
    board[r][c] = player
    flip_pieces(board, r, c, player)
