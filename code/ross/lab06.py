card_number = input("Please input your credit card number: ")

# converts input string into a list then into a list of ints
card_list = list(card_number)
card_list = [int(num) for num in card_list]

# print(card_list)

# removes last digit from list and stores it in a variable (check digit)
check_digit = card_list[-1]
del card_list[-1]
# this could be done more simply with .pop(), per Merritt's example

# print(f"Check digit = {check_digit}")
# print(f"Card list= {card_list}")

# reverses the digits in the list
reversed_list = list(reversed(card_list))

# print(f"reversed list = {reversed_list}")

# doubles every other element in the reversed list
doubled_list = [reversed_list[i] * 2 if i % 2 == 0 else reversed_list[i] for i in range(len(reversed_list))]

# print(f"doubled list = {doubled_list}")

# subtracts nine from numbers over nine
sub_nine = [doubled_list[i] - 9 if doubled_list[i] > 9 else doubled_list[i] for i in range(len(doubled_list))]

# print(f"List subtracting nine from numbers > nine: {sub_nine}")

# sum all values
total = sum(sub_nine)

# print(f"Sum of all values: {total}")

# take the second digit of that sum
second_dig = total % 10
# print(second_dig)

# if that matches the check digit, the whole card number is valid
match = bool(second_dig == check_digit)
# print(match)

if match:
    print("Valid! Thanks.")
else:
    print("Sorry you have entered an invalid number. Please try again.")