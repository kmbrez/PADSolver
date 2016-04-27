"""Optimizer for PAD boards"""
import random


ROWS = 5
COLS = 6
TYPES = 6
COLORS = ["R",
          "B",
          "G",
          "Y",
          "P",
          "H"]
BOARD = [[random.choice(COLORS) for x in range(COLS)] for x in range(ROWS)]  # Randomizing the board


def create_empty_board():
    """Create an empty 5x6 board."""
    return [[0 for x in range(COLS)] for x in range(ROWS)]


def print_board(board):
    """Function to visually print a 5x6 board."""
    for row in board:
        for orb in row:
            print(orb, end="")
        print("")


#def make_rc(row, col):
#	return {"row": row, "col": col}


#def make_match(typing, count, isRow):
#	return {"type": typing, "count": count, "isRow": isRow}


def max_combos(board):
    """This returns the total number of possible matches for each orb type"""
    big_board = []
    for row in board:
        for orb in row:
            big_board.append(orb)
    r_max = int(big_board.count("R") / 3)
    b_max = int(big_board.count("B") / 3)
    g_max = int(big_board.count("G") / 3)
    y_max = int(big_board.count("Y") / 3)
    p_max = int(big_board.count("P") / 3)
    h_max = int(big_board.count("H") / 3)
    big_board = [r_max,
                 b_max,
                 g_max,
                 y_max,
                 p_max,
                 h_max]
    return big_board


def find_matches(board):
    """Using an existing board, this finds all orbs that currently count as a match.
    Recursive function that will keep finding matches until it returns a board with
    no matches remaining.
    """
    matched_orbs = 0
    #find horizontal matches first
    for i in range(0, ROWS):
        prev_2_orb = "X"
        prev_1_orb = "X"
        for j in range(0, COLS):
            cur_orb = board[i][j]
            if (prev_2_orb == prev_1_orb and
                    prev_1_orb == cur_orb and
                    (cur_orb != "X" and cur_orb != " " and cur_orb != 0)):
                board[i][j] = " "
                board[i][j-1] = " "
                board[i][j-2] = " "
                matched_orbs += 1
            prev_2_orb = prev_1_orb
            prev_1_orb = cur_orb

	# find vertical matches
    for j in range(0, COLS):
        prev_2_orb = "X"
        prev_1_orb = "X"
        for i in range(0, ROWS):
            cur_orb = board[i][j]
            if (prev_2_orb == prev_1_orb and
                    prev_1_orb == cur_orb and
                    (cur_orb != "X" and cur_orb != " " and cur_orb != 0)):
                board[i][j] = " "
                board[i-1][j] = " "
                board[i-2][j] = " "
                matched_orbs += 1
            prev_2_orb = prev_1_orb
            prev_1_orb = cur_orb

    # recursion here to re-check the board for more matches after matched orbs are dropped
    if matched_orbs > 0:
        print("Match found. Dropping Orbs.")
        new_board = drop_orbs(board)
        print_board(new_board)
        find_matches(new_board)
    else:
        print("Final board")
        return board

def column_drop(board, match_row, match_col):
    """Takes a board with a row/col coordinate and drops
    the column accordingly.
    """
    next_orb = -1
    for row in range(match_row, 0, -1):
        if board[row-1][match_col] != " ":
            next_orb = row - 1
            break
    if next_orb >= 0:
        board[match_row][match_col] = board[next_orb][match_col]
        for row in range(next_orb, 0, -1):
            board[row][match_col] = board[row-1][match_col]
        board[0][match_col] = " "
    return board


def drop_orbs(board):
    """Takes a board with existing matches and finds
    coordinates for where to drop the board.
    """
    for row in range(ROWS-1, 0, -1):
        for col in range(0, COLS):
            if board[row][col] == " ":
                board = column_drop(board, row, col)
    return board


print_board(BOARD)
print(max_combos(BOARD))
print(sum(max_combos(BOARD)), "combos possible")
find_matches(BOARD)