"""
Doctests:

>>> string_to_int_list('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5')
[4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
>>> get_second_digit(85)
5
>>> double_every_other([5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4])
[10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]
>>> sub_9_if_over_9([10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8])
[1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]
>>> print_valid(5,5)
Valid number
>>> print_valid(1,2)
Invalid number
"""

def string_to_int_list(card_number):
	"""
	returns space-separated string into a list of integers
	"""
	card_number = card_number.split()
	for i in range(len(card_number)):
		card_number[i] = int(card_number[i])
	return card_number


def double_every_other(card_number_list):
	"""
	returns list where every other item is doubled
	"""
	for i in range(0,len(card_number_list),2):
		card_number_list[i] *= 2
	return card_number_list


def sub_9_if_over_9(card_number_list):
	"""
	returns list where if item > 9 then item -= 9
	"""
	for i in range(len(card_number_list)):
		if card_number_list[i] > 9:
			card_number_list[i] -= 9	
	return card_number_list


def get_second_digit(number):
	"""
	returns second digit of number
	"""
	return int(list(str(number))[1])


def print_valid(x, y):
	"""
	inputs: 2 ints
	prints valid if x = y
	"""
	if x == y:
		print('Valid number')
	else:
		print('Invalid number')

def credit_card_validation(card_number):
	"""
	>>> credit_card_validation('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5')
	Valid number
	"""
	card_number = string_to_int_list(card_number)
	check_digit = card_number.pop()
	card_number.reverse()
	card_number = double_every_other(card_number)
	card_number = sub_9_if_over_9(card_number)
	sum_num = sum(card_number)
	second_digit = get_second_digit(sum_num)
	print_valid(second_digit, check_digit)


if __name__ == '__main__':
	credit_card = input("Enter your credit card number: ")
	credit_card_validation(credit_card)
