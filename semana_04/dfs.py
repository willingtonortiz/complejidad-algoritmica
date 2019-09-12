from graph_util import *


def dfs_i(graph, start):
	size = len(graph)
	visited = [False] * size
	path = [None] * size
	stack = [start]

	while len(stack) > 0:
		idx = stack.pop()
		
		if not visited[idx]:
			visited[idx] = True

			for jdx in graph[idx]:
				if not visited[jdx]:
					path[jdx] = idx
					stack.append(jdx)
	print(visited)
	print(path)
	return path


def dfs_r(graph, start):
	size = len(graph)
	visited = [False] * size
	path = [None] * size

	def dfs_r_util(idx):
		if visited[idx]:
			return

		visited[idx] = True
		for idj in graph[idx]:
			if not visited[idj]:
				path[idj] = idx
				dfs_r_util(idj)

	dfs_r_util(0)
	print(visited)
	print(path)
	return path
		


def bfs(graph, start):
	size = len(graph)
	visited = [False] * size
	# (vertex, orden)
	path = [None] * size
	queue = [start]

	while len(queue) > 0:
		idx = queue.pop(0)

		if visited[idx]: continue
		visited[idx] = True

		for idj in graph[idx]:
			if not visited[idj]:
				path[idj] = idx
				queue.append(idj)
	print(visited)
	print(path)
	return path



def run():
	
	# graph = create_graph_list(7)
	graph = [
		[1, 2],
		[3, 4],
		[5, 6],
		[],
		[],
		[],
		[],
	]
	print_graph(graph)
	# bfs(graph, 0)
	dfs_i(graph, 0)
	# dfs_r(graph, 0)
	# print("SEPARATION")



if __name__ == "__main__":
	run()