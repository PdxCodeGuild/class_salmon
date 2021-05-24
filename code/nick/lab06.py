#Credit card validation
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
#I am not sure if this is correct. Everything is coming out invalid, but the example also appears incorrect.