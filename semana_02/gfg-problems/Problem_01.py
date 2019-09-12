# 01. The Knight's tour problem
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


def print_solution(board):
	for row in board:
		print(row)

def clear_board(board):
	for i in range(len(board)):
		for j in range(len(board)):
			board[i][j] = -1

def set_value(board, x, y, val):
	board[y][x] = val

def is_valid_cell(board, x, y):
	if x >= 0 and x < len(board) and y >= 0 and y < len(board) and board[y][x] == -1:
		return True
	return False


def find_one_solution(board):
	board[0][0] = 0
	find_one_solution_util(board, 0, 0, 1)

def find_one_solution_util(board, x, y, pos):
	if pos >= len(board) ** 2:
		print_solution(board)
		return True

	for i in range(8):
		new_x = x + move_x[i]
		new_y = y + move_y[i]
		if is_valid_cell(board, new_x, new_y):
			board[new_y][new_x] = pos

			if find_one_solution_util(board, new_x, new_y, pos + 1):
				return True

			board[new_y][new_x] = -1

	return False


def find_all_solutions(board):
	board[0][0] = 0
	find_all_solutions_util(board, 0, 0, 1)

def find_all_solutions_util(board, x, y, pos):
	if pos >= len(board) ** 2:
		print("/=== SOLUCIÓN ENCONTRADA ===/")
		print_solution(board)
		print("")
		return

	for i in range(8):
		new_x = x + move_x[i]
		new_y = y + move_y[i]
		if is_valid_cell(board, new_x, new_y):
			board[new_y][new_x] = pos

			find_all_solutions_util(board, new_x, new_y, pos + 1)

			board[new_y][new_x] = -1

	return False


def find_one_solution_from_xy(board, x, y):
	board[y][x] = 0
	find_one_solution_util(board, x, y, 1)

def run():
	board_size = 5
	board = [[-1 for i in range(board_size)] for j in range(board_size)]

	# find_one_solution(board)

	for i in range(len(board)):
		for j in range(len(board)):
			print(f"Iniciando en ({j + 1}; {i + 1})")
			find_one_solution_from_xy(board, j, i)
			print("\n")
			clear_board(board)
	


if __name__ == "__main__":
	run()
