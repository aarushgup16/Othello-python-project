from board import EMPTY, BLACK, WHITE, DIRECTIONS, inside

def valid_moves(board, player):
    
    opp = WHITE if player == BLACK else BLACK
    moves = []

    #iterate row/cols explicitly
    for r in range(8):
        for c in range(8):
            if board[r][c] != EMPTY:
                #skipping occupied squares
                continue

            #We'll check the directions and if direction is validates the mode we add it.    
            for direc_row, direc_column in DIRECTIONS:
                rr, cc = r + direc_row, c + direc_column
                found_op = False

                # Move in direction while seeing opp pieces
                while inside(rr, cc) and board[rr][cc] == opp:
                    found_op = True
                    rr += direc_row
                    cc += direc_column

                # If we found opp pieces and end on our own piece, it's moves
                if found_op and inside(rr, cc) and board[rr][cc] == player:
                    moves.append((r, c))
                    break

    return moves


def flip_pieces(board, r, c, player):
    
    opp = WHITE if player == BLACK else BLACK

    for direc_row, direc_column in DIRECTIONS:
        flips = []
        rr, cc = r + direc_row, c + direc_column

        while inside(rr, cc) and board[rr][cc] == opp:
            flips.append((rr, cc))
            rr += direc_row
            cc += direc_column

        # Only flip if the sequence ends in our own piece
        if flips and inside(rr, cc) and board[rr][cc] == player:
            for x, y in flips:
                board[x][y] = player


def make_move(board, r, c, player):
    
    if not inside(r, c):
        return
    
    if board[r][c] != EMPTY:
        return
    
    board[r][c] = player
    flip_pieces(board, r, c, player)