# 02. Rat in a Maze

move_x = [0, 1]
move_y = [1, 0]

def print_matrix(matrix):
	for row in matrix:
		print(row)
		

def is_valid_cell(maze, x, y):
	if x < len(maze) and y < len(maze) and maze[y][x] != 0:
		return True
	return False


def find_one_solution(maze, path, x, y):
	if x == len(maze) - 1 and y == len(maze) - 1:
		return True

	for i in range(2):
		new_x = x + move_x[i]
		new_y = y + move_y[i]
		if is_valid_cell(maze, new_x, new_y):
			path[new_y][new_x] = 1

			if find_one_solution(maze, path, new_x, new_y):
				return True

			path[new_y][new_x] = 0
	
	return False


def run():
	maze_size = 5
	maze = [[1, 0, 0, 0, 0],
			[1, 1, 1, 1, 0],
			[0, 1, 0, 1, 0],
			[0, 1, 0, 1, 0],
			[0, 0, 1, 1, 1]]

	path = [[0 for i in range(maze_size)] for j in range(maze_size)]
	path[0][0] = 1
	
	if find_one_solution(maze, path, 0, 0):
		print("/=== MAZE ===/")
		print_matrix(maze)
		print("\n/=== PATH ===/")
		print_matrix(path)
	else:
		print("No hay solución")
	


if __name__ == "__main__":
	run()
