# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/


def merge_arrays(arra, arrb):
	arrc = [-1 for i in range(len(arra) * 2)]
	i = 0
	j = 0
	k = 0

	while i < len(arra) and j < len(arrb):
		if arra[i] < arrb[j]:
			arrc[k] = arra[i]
			i += 1
		else:
			arrc[k] = arrb[j]
			j += 1
		k += 1

	while i < len(arra):
		arrc[k] = arra[i]
		i += 1
		k += 1
		
	while j < len(arrb):
		arrc[k] = arra[j]
		j += 1
		k += 1

	return arrc


def medianOfTwoSortedArrays(arra, arrb):
	merged_array = merge_arrays(arra, arrb)
	middle = len(merged_array) // 2
	return (merged_array[middle - 1] + merged_array[middle]) // 2


def run():
	arr1 = [1, 12, 15, 26, 38]
	arr2 = [2, 13, 17, 30, 45]
	print(medianOfTwoSortedArrays(arr1, arr2))


if __name__ == "__main__":
	run()
