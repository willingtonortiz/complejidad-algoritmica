

def binary_search(arr, item):
	left = 0
	right = len(arr) - 1

	while(left <= right):
		middle = (right + left) // 2

		if arr[middle] == item:
			return middle
		elif arr[middle] < item:
			left = middle + 1
		elif arr[middle] > item:
			right = middle - 1

	return -1


def run():
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	for i in range(9):
		print(binary_search(arr, i + 1))


if __name__ == "__main__":
	run()
