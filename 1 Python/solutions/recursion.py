# recursion.py
import time


def factorial(n):
	"""
	factorial(n) = n * factorial(n-1)

	>>> factorial(5)
	120
	"""
	if n == 0: # base case
		return 1
	return n * factorial(n-1) # recursive case


# print(factorial(10))

def print_countdown(n):
	if n == 0:
		return 1
	countdown = print_countdown(n-1)
	print(n)
	return countdown


def fibonacci(n):
	"""
	fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

	>>> fibonacci(7)
	13
	"""
	if n == 0:
		return 0
	if n == 1:
		return 1

	return fibonacci(n-1) + fibonacci(n-2)

# for i in range(100):
# 	start = time.time()
# 	print(fibonacci(i))
# 	print(f'calculated {i} fibonacci numbers in {time.time() - start} s')


cached_fibonacci = [0,1]
def memoized_fibonacci(n):
	"""
	fibonacci with memoization

	>>> memoized_fibonacci(100)
	354224848179261915075
	"""
	if n < len(cached_fibonacci):
		return cached_fibonacci[n]
	if n == 0:
		return 0
	if n == 1:
		return 1
	fib = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
	cached_fibonacci.append(fib)
	return fib


start = time.time()
for i in range(200000):
	memoized_fibonacci(i)
print(f'calculated the first 200000 fibonacci numbers in {time.time() - start} s')
print('the 200000th fibonacci number is', memoized_fibonacci(200000))


def binary_search(l, target, start, end):
	"""
	l: list
	target: num or word
	start: start idx
	end: end idx
	searches sorted list l for target

	>>> binary_search([1,2,3,4,5,6,7], 7, 0, 7)
	6
	"""
	if start >= end:
		return 'Not found'

	mid = start + (end - start)//2
	# print(target, l[mid], start, end)
	if l[mid] == target:
		return mid

	if l[mid] < target:
		return binary_search(l, target, mid+1, end)

	if target < l[mid]:
		return binary_search(l, target, start, mid)


if __name__ == '__main__':
	pass

