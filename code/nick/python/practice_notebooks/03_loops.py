

# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled
nums = [1,2,3,4,5]
def double_numbers(nums):
    y = []
    for num in nums:
        if num %2 == 0:
            nums = 2 * num
            y.append(nums)
        #if the number in nums does not divide evenly by 2 then add num to empty list y
        elif num %2 != 0:
            nums = num
            y.append(nums)
    #return the newly filled list y
    return y
print(double_numbers(nums))
            
# print(double_numbers(nums))
# def test_double_numbers():
#     assert double_numbers([1, 2, 3]) == [4, 5, 6]


# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n):
    asterisks_list = []
    for count in range(n):
        asterisks_list += '*'
    return asterisks_list
print(stars(10))

# # def test_stars():
#     assert stars(1) == '*'
#     assert stars(2) == '**'
#     assert stars(3) == '***'
#     assert stars(4) == '****'


# # Extract Less Than Ten
# # Write a function to move all the elements of a list with value less than 10 to a new list and return it.

# def extract_less_than_ten(nums):
#     ...

# def test_extract_less_than_ten(nums):
#     extract_less_than_ten([2, 8, 12, 18]) == [2, 8]



