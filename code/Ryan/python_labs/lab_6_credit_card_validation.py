"""
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
"""
# # User input
# credit_card_input = input("Enter a credit card number: ")
# #print(f"Line 21 {credit_card_input}")
# # Convert the input string into a list of ints
# credit_card_input_list = list(map(int,credit_card_input))
# #print(f"Line 24 {credit_card_input_list}")
# # Slice off the last digit. That is the check digit.
# check_digit = credit_card_input_list.pop(-1)
# #print(f"Line 27 {check_digit}")
# # Reverse the digits.
# credit_card_input_list.reverse()
# #print(f"Line 30 {credit_card_input_list}")
# # Double every other element in the reversed list.
# doubled_elements = []
# for each_element in credit_card_input_list[::2]:
#     doubled_element = each_element * 2

#     # Subtract nine from numbers over nine.
#     if doubled_element > 9:
#         doubled_element = doubled_element - 9
#         #doubled_elements.append(doubled_element)
#     else:
#         #doubled_elements.append(doubled_element)
#         None

# # Sum all values.
# total_value = 0

# for each_element in credit_card_input_list:
#     total_value += each_element

# # Take the second digit of that sum.
# total_value = str(total_value)
# sum_second_digit = total_value[1]

# # If that matches the check digit, the whole card number is valid.
# check_digit = str(check_digit)

# if sum_second_digit == check_digit:
#     print("Valid credit card")
# else:
#     print("Invalid card number")


# #print(credit_card_input_list)
# #print(check_digit)
# #print(every_other_element_credit_card_list)
# #print(doubled_elements)
# #print(total_value)
# #print(sum_second_digit)

numbers = input("Enter credit card number: ")
#print(numbers)
numbers_list = []
for each_number in numbers:
    numbers_list.append(each_number)
#print(numbers_list)
check_digit = numbers_list.pop(-1)
#print(numbers_list)
numbers_list.reverse()
even_i_numbers = []
odd_i_numbers = []
for i in range(len(numbers_list)):
    #print(i, numbers_list[i])
    if i % 2 == 0:
        even_i_numbers.append(numbers_list[i])
    else:
        odd_i_numbers.append(numbers_list[i])

#print(odd_i_numbers)
#print(even_i_numbers)
doubled_numbers = []
for i_numbers in even_i_numbers:
    #print(type(i_numbers))
    i_numbers = int(i_numbers)
    doubled_numbers.append(i_numbers*2)

#print(doubled_numbers)
doubled_numbers_after_minus_nine = []
for each_doubled_number in doubled_numbers:

    if each_doubled_number > 9:
        result = each_doubled_number - 9
        doubled_numbers_after_minus_nine.append(result)
    else:
        doubled_numbers_after_minus_nine.append(each_doubled_number)

#print(doubled_numbers_after_minus_nine)

new_numbers = []
for each_number in doubled_numbers_after_minus_nine:
    new_numbers.append(each_number)
for each_number in odd_i_numbers:
    new_numbers.append(int(each_number))

#print(new_numbers)
sum = 0
for each_number in new_numbers:
    sum += each_number
#print(sum)

sum_2 = sum % 10
#print(sum_2)

if str(sum_2) == check_digit:
    print("Valid Card Number")
else:
    print("Invalid card number")
#sum = str(sum)
#new_sum = map(str, sum)
#print(new_sum)


