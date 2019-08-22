# N Queen Problem Backtracking 3

def print_matrix(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == -1:
				print("_", end = ' ')
			else:
				print("Q", end = ' ')
		print("")


def is_valid_cell(board, col, row):
	for i in range(col):
		if board[row][i] != -1:
			return False

	for j in range(col):
		for i in range(len(board)):
			if board[i][j] != -1 and abs(i - row) == abs(j - col):
				return False

	return True


def find_one_solution(board, col, queens):
	if queens == 4:
		return True

	for row in range(len(board)):
		if is_valid_cell(board, col, row):
			board[row][col] = 1

			if find_one_solution(board, col + 1, queens + 1):
				return True

			board[row][col] = -1

	return False


def find_all_solutions(board, col, queens):
	if queens == len(board):
		print("/=== START SOLUTION ===/")
		print_matrix(board)
		print("/=== END SOLUTION ===/\n")
		return

	for row in range(len(board)):
		if is_valid_cell(board, col, row):
			board[row][col] = 1

			find_all_solutions(board, col + 1, queens + 1)

			board[row][col] = -1


def count_all_solutions(board, col, queens):
	if queens == len(board):
		return 1
	
	counter = 0

	for row in range(len(board)):
		if is_valid_cell(board, col, row):
			board[row][col] = 1

			counter += count_all_solutions(board, col + 1, queens + 1)

			board[row][col] = -1
	
	return counter


def run():
	size = 4
	board = [[-1 for i in range(size)] for j in range(size)]

	if find_one_solution(board, 0, 0):
		print_matrix(board)
	else:
		print("No hay solución")


def run_all_solutions():
	size = 12
	board = [[-1 for i in range(size)] for j in range(size)]

	find_all_solutions(board, 0, 0)
	counter = count_all_solutions(board, 0, 0)

	print(f"Numero de soluciones {counter}")


if __name__ == "__main__":
	# run()
	run_all_solutions()

