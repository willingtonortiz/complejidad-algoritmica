import math
import random


def generate(n):
	return [random.randint(1, 100) for i in range(n)]


def display(array):
	print(array)


def reverse(array):
	return array[::-1]


def array_min(array):
	return min(array)


def array_average(array):
	return sum(array) / len(array)


def count_ocurrencies(array):
	counter = [0 for i in range(len(array) + 1)]

	for i in array:
		counter[i] += 1

	return counter


def ocurrencies_average(ocurrencies):
	total = 0
	counter = 0

	for i, val in enumerate(ocurrencies):
		total += i * val
		counter += val

	return total / counter


def run():
	arr = generate(100)
	print(array_min(arr))
	print(array_average(arr))
	# print(count_ocurrencies(arr))
	print(ocurrencies_average(count_ocurrencies(arr)))


if __name__ == "__main__":
	run()
