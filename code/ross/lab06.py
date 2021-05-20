card_number = input("Please input your credit card number: ")

# converts input string into a list then into a list of ints
card_list = list(card_number)
card_list = [int(num) for num in card_list]

print(card_list)

# removes last digit from list and stores it in a variable (check digit)
check_digit = card_list[-1]
del card_list[-1]

print(f"Check digit = {check_digit}")
print(f"Card list= {card_list}")

# reverses the digits in the list
reversed_list = list(reversed(card_list))

print(f"reversed list = {reversed_list}")

# doubles every other element in the reversed list
doubled_list = [num * 2 for num in reversed_list]


print(f"doubled list = {doubled_list}")

# subtracts nine from numbers over nine

# sum all values

# take the second digit of that sum

# if that matches the check digit, the whole card number is valid