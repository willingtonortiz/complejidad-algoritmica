# 07. Sudoku


def is_valid_sudoku(matrix):
	# Validación por filas
	for i in range(9):
		occur = [False for i in range(10)]
		for j in range(9):
			if occur[matrix[i][j]]:
				return False
			occur[matrix[i][j]] = True
			
	# Validación por columnas
	for j in range(9):
		occur = [False for i in range(10)]
		for i in range(9):
			if occur[matrix[i][j]]:
				return False
			occur[matrix[i][j]] = True
	
	# Validación por grillas
	for i in range(3):
		for j in range(3):
			occur = [False for i in range(10)]
			for k in range(3):
				for l in range(3):
					if occur[matrix[i * 3 + k][j * 3 + l]]:
						return False
					occur[matrix[i * 3 + k][j * 3 + l]] = True

	return True


def print_matrix(matrix):
	for row in matrix:
		print(row)


def read_file():
	with open("input.txt") as f:
		content = f.readlines()
		matrix = []
		for line in content:
			row = [int(val) for val in line.split()]
			matrix.append(row)
		return matrix


def is_valid_cell(matrix, row, col, val):
	for i in range(9):
		if matrix[row][i] == val:
			return False

	for i in range(9):
		if matrix[i][col] == val:
			return False
	
	# print(row // 3, col // 3)
	row = (row // 3) * 3
	col = (col // 3) * 3
	# print(row, col)
	for i in range(3):
		for j in range(3):
			if matrix[row + i][col + j] == val:
				return False

	return True


def find_next_cell(row, col):
	if col + 1 == 9:
		return row + 1, 0
	else:
		return row, col + 1


def find_one_solution(sudoku, row, col):
	if row == 9:
		print_matrix(sudoku)
		return True

	if sudoku[row][col] != -1:
		n_row, n_col = find_next_cell(row, col)
		if find_one_solution(sudoku, n_row, n_col):
			return True
	else:
		for i in range(1, 10):
			if is_valid_cell(sudoku, row, col, i):
				sudoku[row][col] = i

				n_row, n_col = find_next_cell(row, col)
				if find_one_solution(sudoku, n_row, n_col):
					return True

				sudoku[row][col] = -1

	return False

def find_all_solutions(sudoku, row, col):
	if row == 9:
		print("/=== INICIO SOLUCIÓN ===/")
		print_matrix(sudoku)
		print("/=== FIN ===/\n")
		return

	if sudoku[row][col] != -1:
		n_row, n_col = find_next_cell(row, col)
		find_all_solutions(sudoku, n_row, n_col)
	else:
		for i in range(1, 10):
			if is_valid_cell(sudoku, row, col, i):
				sudoku[row][col] = i

				n_row, n_col = find_next_cell(row, col)
				find_all_solutions(sudoku, n_row, n_col)

				sudoku[row][col] = -1
	return


def run():
	matrix = read_file()
	# find_one_solution(matrix, 0, 0)
	find_all_solutions(matrix, 0, 0)


if __name__ == "__main__":
	run()



# 3 -1 6 5 -1 8 4 -1 -1
# 5 2 -1 -1 -1 -1 -1 -1 -1
# -1 8 7 -1 -1 -1 -1 3 1
# -1 -1 3 -1 1 -1 -1 8 -1
# 9 -1 -1 8 6 3 -1 -1 5
# -1 5 -1 -1 9 -1 6 -1 -1
# 1 3 -1 -1 -1 -1 2 5 -1
# -1 -1 -1 -1 -1 -1 -1 7 -1
# -1 -1 5 2 -1 6 3 -1 -1


# 8 -1 -1 -1 -1 -1 -1 -1 -1
# -1 -1 3 6 -1 -1 -1 -1 -1
# -1 7 -1 -1 9 -1 2 -1 -1
# -1 5 -1 -1 -1 7 -1 -1 -1
# -1 -1 -1 -1 4 5 7 -1 -1
# -1 -1 -1 1 -1 -1 -1 3 -1
# -1 -1 1 -1 -1 -1 -1 6 8
# -1 -1 8 5 -1 -1 -1 1 -1
# -1 9 -1 -1 -1 -1 4 -1 -1