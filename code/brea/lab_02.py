numbers = []
print('Let\'s average some numbers!')
while True:
    user_input = input("Enter a number to add to the list, enter 'done' when finished: ").lower()
    numbers.append(user_input)
    if user_input == 'done':
        break
numbers.remove('done')  

print('The list of numbers you entered was: ')
for item in numbers:
    print(item)
sum = 0

for item in numbers:
   sum += int(item) 
print(f'The sum of the list of numbers was: {sum} ')     
avg = sum / len(numbers)
print(f'The average of the list is: {avg}')