"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 06
Version: 1
Date: 5/20/2021

"""
# "4888937101804229"
# Get CC # as input
cc_num = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5"  # input("Enter CC number: ")

# check for and remove any dashes or spaces if entered:
cc_num = cc_num.replace("-", "")
cc_num = cc_num.replace(" ", "")
print(f"Check spacing: {cc_num}")

# Convert from string to list of ints
cc_num = [int(number) for number in cc_num]
print(f"Check list of ints: {cc_num}")

# get check digit and remove
check_digit = cc_num.pop(-1)
print(f"Check Digit: {check_digit}")
print(f"Check digit removed: {cc_num}")

# Reverse the list.
cc_num.reverse()
print(f"List reversed: {cc_num}")
original_nums = [number for number in cc_num]
# Double every other element
counter = 0
while counter < len(cc_num):
    print(f"Index: {counter} Modulus: {counter % 2}")
    if counter % 2 == 0:
        cc_num[counter] *= 2
        counter += 1
    else:
        counter += 1
print(f"        Original List: {original_nums}")
print(f"Even elements doubled: {cc_num}")

# Subtract 9 from numbers over 9
cc_num = [(number - 9 if number > 9 else number) for number in cc_num]
print(f"           Subtract 9: {cc_num}")

# Sum all values
cc_num = sum(cc_num)
print(f"Sum: {cc_num}")

if cc_num > 9:
    print(cc_num % 10 == check_digit)
else:
    print(cc_num == check_digit)
