
def replace_letters(letters_map, word):
	num = 0
	for letter in word:
		num *= 10
		num += letters_map[letter]
	return num


def is_valid_operation(letters_map, words):

	words_sum = 0
	total = replace_letters(letters_map, words[-1])

	for word in words[:-1]:
		words_sum += replace_letters(letters_map, word)

	if words_sum == total:
		return True
	return False


def make_letters_map(words):
	new_map = {}
	for word in words:
		for letter in word:
			new_map[letter] = -1
	return new_map


def is_valid_number(letters_map, letter, number, words):
	# Si el número está en el mapa
	if number in letters_map.values():
		return False

	# Si el número es cero y existe alguna palabra inicie con esa letra
	for word in words:
		if number == 0 and letter == word[0]:
			return False

	return True


def find_one_solution_util(letters_map, letters, idx, words):
	if len(letters) == idx:
		if is_valid_operation(letters_map, words):
			print(letters_map)
			return True
		else:
			return False

	for i in range(10):
		current_letter = letters[idx]

		if is_valid_number(letters_map, current_letter, i, words):
			letters_map[current_letter] = i

			if find_one_solution_util(letters_map, letters, idx + 1, words):
				return True

			letters_map[current_letter] = -1

	return False


def find_one_solution():
	# words = ["SEND", "MORE", "MONEY"]
	# words = ["DOS", "DOS", "TRES", "SIETE"]
	# words = ["ABCD", "EBCB", "AFGAG"]
	# words = ["GOOD", "DOG", "OREO"]
	# words = ["GOAT", "AAA", "ERROR"]
	# words = ["CP", "IS", "FUN", "TRUE"]
	words = ["BASE", "BALL", "GAMES"]

	letters_map = make_letters_map(words)
	letters = list(letters_map.keys())

	print(words)
	print(letters_map)
	print(letters)

	find_one_solution_util(letters_map, letters, 0, words)


def run():
	find_one_solution()


if __name__ == "__main__":
	run()

# SEND + MORE = MONEY
#  'S': 2,
#  'E': 8,
#  'N': 1,
#  'D': 7,
#  'M': 0,
#  'O': 3,
#  'R': 6,
#  'Y': 5

# DOS + DOS + TRES = SIETE
# 'D': 5,
# 'O': 8,
# 'S': 1,
# 'T': 9,
# 'R': 2,
# 'E': 3,
# 'I': 0

#   DOS   581
#   DOS   581
#  TRES  9231
# SIETE 10393


# EINS + EINS + EINS = VIER
