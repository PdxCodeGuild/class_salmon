user_input = input("Please enter a number, or 'done': ")
nums = []
total = 0

# this section adds numbers to the list until a user tells it they're done
while user_input != 'done':
    nums.append(int(user_input))
    user_input = input("Please enter a number, or 'done': ")

# this creates a sum of all the entered numbers and stores it in a variable called 'total'
for num in nums:
    total += num

print(f"You entered {len(nums)} numbers and the average of your numbers is: {total / len(nums)}")