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
# User input
credit_card_input = input("Enter a credit card number: ")
#print(f"Line 21 {credit_card_input}")
# Convert the input string into a list of ints
credit_card_input_list = list(map(int,credit_card_input))
#print(f"Line 24 {credit_card_input_list}")
# Slice off the last digit. That is the check digit.
check_digit = credit_card_input_list.pop(-1)
#print(f"Line 27 {check_digit}")
# Reverse the digits.
credit_card_input_list.reverse()
#print(f"Line 30 {credit_card_input_list}")
# Double every other element in the reversed list.
doubled_elements = []
for each_element in credit_card_input_list[::2]:
    doubled_element = each_element * 2

    # Subtract nine from numbers over nine.
    if doubled_element > 9:
        doubled_element = doubled_element - 9
        #doubled_elements.append(doubled_element)
    else:
        #doubled_elements.append(doubled_element)
        None

# Sum all values.
total_value = 0

for each_element in credit_card_input_list:
    total_value += each_element

# Take the second digit of that sum.
total_value = str(total_value)
sum_second_digit = total_value[1]

# If that matches the check digit, the whole card number is valid.
check_digit = str(check_digit)

if sum_second_digit == check_digit:
    print("Valid credit card")
else:
    print("Invalid card number")


#print(credit_card_input_list)
#print(check_digit)
#print(every_other_element_credit_card_list)
#print(doubled_elements)
#print(total_value)
#print(sum_second_digit)
