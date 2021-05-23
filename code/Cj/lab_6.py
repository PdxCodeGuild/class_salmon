

card_number = '4556737586899855'
card_number = list(card_number)
output_number = []
for i in card_number:
    i = int(i)
    output_number.append(i)   
check_digit = output_number.pop(-1)
output_number.reverse()
print(output_number)
for i, value in enumerate(output_number):
    if i % 2 == 0:
        pass
    else:
      output_number(value) += output_number(value)
   
   

print(output_number)

# def validate(card_number):
#     card_number = list(int(card_number))
#     for i in card_number:
#         i = int(i)
#         output_number.append(i)
#     check_digit = card_number.pop[-1]
#     card_number = card_number.reverse()
#     for i in card_number:
#         if i % 2 == 0:
#             i *= 2

# card_number = input('Enter Credit Card Number: ')




