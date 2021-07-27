number_input = int(input("Enter a number "))

ones_digit = number_input % 10
tens_digit = number_input // 10

if ones_digit == 1:
  ones_digit_string = 'one'


conversion_dict = {
  67: 'sixty-seven'
}

one_through_ten = {
  1: 'one',
  2: 'two'
}

# combine tens digit filtered through tens dict with ones digit filtered through ones dict

print(one_through_ten[ones_digit])