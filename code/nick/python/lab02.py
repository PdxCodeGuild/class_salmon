nums = [5, 0, 8, 3, 4, 1, 6]
'''
# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])
'''
#Average a sum of the list
'''sum_num = 0
for num in nums:
    sum_num += num
    print(sum_num)
num_nums = len(nums)
average_nums = sum_num/num_nums
print(f"The average of the sum of numbers is {average_nums}")
'''
#Version 2
#ask user to enter numbers into list
#when done then display average


list = []
boolean = True
while boolean == True:
    num_or_done = input("Enter a number or 'done'")
    if num_or_done.isnumeric():
        list.append(float(num_or_done))
    elif num_or_done == 'done':
        boolean = False
        break

average_from_user = sum(list)/len(list)
print(f'The average of your list values are {average_from_user}.')