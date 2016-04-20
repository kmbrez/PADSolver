﻿"""Optimizer for PAD boards"""
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
    Returns a board that only shows matched orbs.
    """
    match_board = create_empty_board()
    #find horizontal matches first
    for i in range(0, ROWS):
        prev_2_orb = "X"
        prev_1_orb = "X"
        for j in range(0, COLS):
            cur_orb = board[i][j]
            if prev_2_orb == prev_1_orb and prev_1_orb == cur_orb and (cur_orb != "X" or cur_orb != 0):
                match_board[i][j] = cur_orb
                match_board[i][j-1] = cur_orb
                match_board[i][j-2] = cur_orb
                board[i][j] = 0
                board[i][j-1] = 0
                board[i][j-2] = 0
            prev_2_orb = prev_1_orb
            prev_1_orb = cur_orb

	#find vertical matches
    for j in range(0, COLS):
        prev_2_orb = "X"
        prev_1_orb = "X"
        for i in range(0, ROWS):
            cur_orb = board[i][j]
            if prev_2_orb == prev_1_orb and prev_1_orb == cur_orb and (cur_orb != "X" or cur_orb != 0):
                match_board[i][j] = cur_orb
                match_board[i-1][j] = cur_orb
                match_board[i-2][j] = cur_orb
                board[i][j] = 0
                board[i-1][j] = 0
                board[i-2][j] = 0
            prev_2_orb = prev_1_orb
            prev_1_orb = cur_orb

    #count number of matched orbs in every column
    matched_orbs = 0
    for x in range(0, COLS):
        for y in range(0, ROWS):
            if board[y][x] == 0:
                matched_orbs += 1
    print(matched_orbs, "orbs matched")
    print_board(board)
    if matched_orbs > 0:
        find_matches(drop_orbs(board))
    else:
        return match_board


def drop_orbs(board):
    """Takes a board with existing matches and drops
    the board accordingly.
    """



print_board(BOARD)
print(max_combos(BOARD))
print(sum(max_combos(BOARD)), "combos possible")
find_matches(BOARD)
