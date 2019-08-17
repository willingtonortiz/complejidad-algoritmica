
def read_matrix():
	matrix = [[int(x) for x in input().split()] for y in range(9)]
	return matrix


def validate_sudoku(matrix):
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


def run():
	print("Ingrese el sudoku: ")

	grid = read_matrix()

	is_valid = validate_sudoku(grid)

	if(is_valid):
		print("El sudoku ingresado es correcto")
	else:
		print("El sudoku ingresado es incorrecto")



if __name__ == "__main__":
	run()




# 7 4 3 9 5 1 6 8 2
# 1 6 2 4 8 7 3 9 5
# 9 5 8 6 3 2 7 1 4
# 2 1 9 8 7 3 5 4 6
# 3 7 4 5 6 9 1 2 8
# 5 8 6 1 2 4 9 7 3
# 4 9 5 2 1 6 8 3 7
# 8 2 7 3 9 5 4 6 1
# 6 3 1 7 4 8 2 5 9