# 04. Sumset Sum


# [0, 0, 0, 0, 0, 0, 0]

def find_one_solution(arr, data, sum_w, sum_a, idx):
	if sum_w == sum_a:
		print(arr)
		print(data)
		return True

	if sum_a > sum_w:
		return False

	for i in range(idx, len(arr)):
		data[i] = arr[i]

		if find_one_solution(arr, data, sum_w, sum_a + arr[i], idx + 1):
			return True

		data[i] = 0
	return False


def find_all_solutions(arr, data, sum_w, sum_a, idx):
	if sum_a > sum_w:
		return 0

	if sum_a == sum_w:
		print(data)
		return 1
	
	counter = 0

	for i in range(idx, len(arr)):
		data[i] = arr[i]
		counter += find_all_solutions(arr, data, sum_w, sum_a + arr[i], i + 1)
		data[i] = 0

	return counter



def run():
	# weights = [10, 7, 5, 18, 12, 20, 15]
	# weights = [15, 22, 14, 26, 32, 9, 16, 8]
	# weights = [5, 16, 3, 2]
	weights = [3, 34, 4, 12, 5, 2]
	sum_w = 9
	size = len(weights)
	data = [0 for i in range(size)]

	# find_one_solution(weights, data, sum_w, 0, 0)
	counter = find_all_solutions(weights, data, sum_w, 0, 0)

	print(f"Soluciones: {counter}")


if __name__ == "__main__":
	run()
