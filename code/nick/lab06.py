'''#Credit card validation
input_string = input('What is the credit card number?')
#convert from string to list
input_list = list(input_string)
print(input_list)
#list of strings to list of integers
input_list_integers = [int(i) for i in input_list]
print(input_list_integers)
#slice off the last digit
removed_input = input_list_integers.pop(-1)
print(removed_input)
print(input_list_integers)
#reverse the digits
reversed_input = list(reversed(input_list_integers))
print(reversed_input)
#double each number in the reversed list
doubled_reversed_input = [i*2 for i in reversed_input]
print(doubled_reversed_input)
subtracted_doubled_reversed_input= [doubled_reversed_input[i]-9 if doubled_reversed_input[i]>9 else doubled_reversed_input[i] for i in range(len(doubled_reversed_input))]
#this took me many attempts, remember "for i in range(len(variable))"
print(subtracted_doubled_reversed_input)
#sum all the values
summed_values = sum(subtracted_doubled_reversed_input)
print(summed_values)
#take the second digit off of sum
summed_values_list = list(str(summed_values))
print(summed_values_list)
integers_summed_values_list = [int(i) for i in summed_values_list]
print(integers_summed_values_list)
removed_digit_summed_values_list = integers_summed_values_list.pop(-1)
print(removed_digit_summed_values_list)
if removed_digit_summed_values_list == removed_input:
    print('Valid!')
else:
    print('Invalid!')
#I am not sure if this is correct.
#update. I am an idiot. I did not double everyother digit. I doubled every digit
#merritt's demonstration
def cc_validation(original_number):
    list_of_ints = list(original_number)
    #better to allow the number of digits to vary with the input
    for i in range(len(list_of_ints)):
        list_of_ints[i] = int(list_of_ints[i])
    #remove the last digit save it to variable
    check_digit = list_of_ints.pop()
    #reverses in place
    list_of_ints.reverse()

    for i in range(len(list_of_ints)):
        #if index divisible by 2
        if i % 2 == 0:
            list_of_ints[i] *=2
    for i in range(len(list_of_ints)):
        if list_of_ints[i] > 9:
            list_of_ints[i] -= 9
    
    #use built-in sum funct
    list_of_ints_sum = sum(list_of_ints)
    #get the remainder of the sum
    second_digit_of_sum = list_of_ints_sum % 10
    
    return second_digit_of_sum == check_digit
print(cc_validation('4556737586899855'))
'''
# a better way to do it all
def cc_valid(original_number):
    list_of_original_number = list(original_number)
    list_of_ints = [int(num) for num in list_of_original_number]
    #pop removes the last digit by default, unless specified
    check_digit = list_of_ints.pop()
    #
    reversed_digits = list(reversed(list_of_ints))
    #needs to have the same numbers going into the list comprehension as coming out
    #if the digit is divisible by 2, then double the digit for each index i
    every_other_doubled = [(digit * 2 if i %2 ==0) for i, digit in enumerate(reversed_digits)]