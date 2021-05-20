numbers = [] # defining a variable as a list
print('Let\'s average some numbers!') # printing a string
while True: # start of while loop for averaging numbers
    user_input = input("Enter a number to add to the list, enter 'done' when finished: ").lower() # defining a variable and inputting data into list
    numbers.append(user_input) # adding to the end of the list
    if user_input == 'done': # if statement checking to see if input equals done
        break # breaks loop
numbers.remove('done')  # removes the word done from the list

print('The list of numbers you entered was: ') # printing a string 
for item in numbers: # for loop starting codeblock
    print(item) # prints items of the list
sum = 0 # defining a variable

for item in numbers: # for loop starting codeblock for averaging
   sum += int(item)  # variable is added to the items and making items an integer
print(f'The sum of the list of numbers was: {sum} ')  # printing the sum of the items in the list
avg = sum / len(numbers) # generating the average
print(f'The average of the list is: {avg}') # f string containing a statement and the average