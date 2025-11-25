# Othello Overview
This Python project is a full implementation of the Othello game using 2D lists and turn-based logic. It detects valid moves in all 8 directions, flips opponent pieces automatically, tracks scores, handles invalid moves, skips turns when needed, and announces the final winner after counting discs.

# Rules
A valid move must:
Be placed on an empty square.
Sandwich one or more opponent pieces between the newly placed disc and another disc of yours.
The sandwich can be in any of the 8 directions:
Horizontal (left/right)
Vertical (up/down)
Diagonal
If a move does not capture at least one opponent piece → ❌ not allowed.

# Strategy Tips
| Beginner Tips                    | Advanced Strategy                     |
| -------------------------------- | ------------------------------------- |
| Take safe moves                  | Corners are the most valuable         |
| Avoid edges early                | Control mobility (valid move options) |
| Don’t flip too many pieces early | Force opponent into bad moves         |
