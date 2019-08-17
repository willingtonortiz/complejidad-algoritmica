
class EratosthenesSieve:

	def generate_sieve(self, number):
		sieve = [True for i in range(number)]
		sieve[0] = sieve[1] = False

		for i in range(2, int(number ** 0.5)):
			if sieve[i]:
				for j in range(i * i, number, i):
					sieve[j] = False

		return sieve


	def sieve_generator(self, number):
		sieve = self.generate_sieve(number)

		for i in range(2, number):
			if sieve[i]:
				yield i


	def count_primes_less_than(self, number):
		sieve = self.generate_sieve(number)
		prime_numbers_counter = 0

		for i in range(2, number):
			prime_numbers_counter += sieve[i]
		
		return prime_numbers_counter



class Series:

	def multiple_generator(self, number):
		index = 0
		while True:
			yield index * number
			index += 1

	
	def fibonacci_generator(self):
		a = 0
		b = 1

		yield 0
		while True:
			a, b = b, a + b
			yield a


def generator_main():
	series = Series()
	
	print("/* Multiplos de 3 */")
	multiple_3 = series.multiple_generator(3)
	for _ in range(5):
		print(next(multiple_3))


	print("/* Números de Fibonacci */")
	fibonacci = series.fibonacci_generator()
	for _ in range(5):
		print(next(fibonacci))


def prime_main():
	eratosthenesSieve = EratosthenesSieve()
	number = int(input("Ingrese un número: "))

	prime_numbers_counter = eratosthenesSieve.count_primes_less_than(number)

	print(prime_numbers_counter)


def sieve_main():
	eratosthenesSieve = EratosthenesSieve()
	criba = eratosthenesSieve.sieve_generator(10)

	for val in criba:
		print(val)


if __name__ == "__main__":
	# generator_main()
	# prime_main()
	sieve_main()
