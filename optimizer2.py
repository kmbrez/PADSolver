import random


ROWS = 5
COLS = 6
TYPES = 6
COLORS = ["R", "B", "G", "Y", "P", "H"]
Board = [[random.choice(COLORS) for x in range(COLS)] for x in range(ROWS)]  # Randomizing the board

def create_empty_board():
	return [[0 for x in range(COLS)] for x in range(ROWS)]


def print_board(Board):
	for row in Board:
		print(row)


def make_rc(row, col):
	return {"row": row, "col": col}


def make_match(typing, count, isRow):
	return {"type": typing, "count": count, "isRow": isRow}


def max_combos(Board):
	big_board = []
	for row in Board:
		for orb in row:
			big_board.append(orb)
	r_max = int(big_board.count("R") / 3)
	b_max = int(big_board.count("B") / 3)
	g_max = int(big_board.count("G") / 3)
	y_max = int(big_board.count("Y") / 3)
	p_max = int(big_board.count("P") / 3)
	h_max = int(big_board.count("H") / 3)
	return [r_max, b_max, g_max,
			y_max, p_max, h_max]


def find_matches(Board):
	match_board = create_empty_board()
	matches = 0
	#find horizontal matches first
	for i in range(0, ROWS):
		prev_1_orb = "X"
		prev_2_orb = "X"
		for j in range(0, COLS):
			cur_orb = Board[i][j]
			if (prev_1_orb == prev_2_orb and prev_2_orb == cur_orb and cur_orb != "X"):
				match_board[i][j] = cur_orb
				match_board[i][j-1] = cur_orb
				match_board[i][j-2] = cur_orb
			prev_1_orb = prev_2_orb
			prev_2_orb = cur_orb

	#find vertical matches
	for j in range(0, COLS):
		prev_1_orb = "X"
		prev_2_orb = "X"
		for i in range(0, ROWS):
			cur_orb = Board[i][j]
			if (prev_1_orb == prev_2_orb and prev_2_orb == cur_orb and cur_orb != "X"):
				match_board[i][j] = cur_orb
				match_board[i-1][j] = cur_orb
				match_board[i-2][j] = cur_orb
			prev_1_orb = prev_2_orb
			prev_2_orb = cur_orb
	return match_board


print_board(Board)
print(max_combos(Board), sum(max_combos(Board)))
for row in find_matches(Board):
    print(row)
