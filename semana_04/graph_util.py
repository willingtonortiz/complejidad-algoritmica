import random


def print_graph(graph):
	for idx, row in enumerate(graph):
		print(idx, "=>", row)


def create_graph_list(size):
	graph = []
	for i in range(size):
		row = set()

		for j in range(random.randint(0, size)):
			row.add(random.randint(0, size - 1))
		graph.append(list(set(row)))
	return graph