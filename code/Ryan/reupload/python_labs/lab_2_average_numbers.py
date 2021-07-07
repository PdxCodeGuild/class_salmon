# Lab 10: Average Numbers
# Problem: Average a list of numbers

# ---------------------------- V2 --------------------------------#

# Start with list
nums = []

# Keep running sum
running_sum = 0

# If calculate does not equal True, calculate the average
calculate = True

while calculate:
    # Ask user to enter numbers one at a time
    # Put numbers into list
    nums_input = input("Enter a number or 'done' to calculate: ")

    if nums_input != "done":
        nums.append(int(nums_input))

    elif nums_input == "done":
        calculate = False
        break

# Add each number to numbers list
for num in nums:
    running_sum += num

# Divide sum by number of elements
nums_count = len(nums)
print(f"""
Total sum: {running_sum}
Number of elements: {nums_count}
Numbers entered: {nums}
""")

# Calculate average
average = running_sum / float(nums_count)
print(f"The average of the list is {average}")