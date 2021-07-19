#Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number 
# and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.
for nums in range(1,101):
    if nums%3==0 and nums%5==0:
        nums="FizzBuzz"    
    elif nums%3==0:
        nums="fizz"
    elif nums%5==0:
        nums="buzz"
    print(nums)