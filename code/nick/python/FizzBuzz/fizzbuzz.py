#Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number 
# and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.
for num in range(1,101):
    if num%3==0 and num%5==0:
        num="FizzBuzz"    
    elif num%3==0:
        num="fizz"
    elif num%5==0:
        num="buzz"
    print(num)