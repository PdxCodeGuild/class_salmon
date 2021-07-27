# user input credit card number
user_cc = input("Please enter your credit card number: ")
# convert to list of integers
cc_number_list = [int(x) for x in str(user_cc)]
# remove and assign last number to check variable
check_digit = cc_number_list.pop(15)
# reverse the 15 digit list
cc_number_list.reverse()
# double every other digit
double_list = cc_number_list[:]
double_list[::2] = [x*2 for x in double_list[::2]]
# isolates numbers greater than 9 and subtracts 9
nine_list = [y - 9 for y in double_list if y > 9]
# isolates numbers less than 9 and assigns them to a new list
less_than_nine_list = [z - 0 for z in double_list if z <= 9]
# adds the two lists together
new_list = nine_list + less_than_nine_list
# sum the new list
sum_list = sum(new_list)
# finds the last digit of the sum list
check_sum = sum_list % 10
if check_sum == check_digit:
    print("Valid! Thank you.")
else:
    print("Sorry that is not a valid credit card number.")    