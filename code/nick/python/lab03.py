#convert a numeric value to written english form [0-99].
#Version 1
#ask a question
num_in = int(input('What number would you like converted to english[0-99]?'))
#make a dictionary for the ones
one_place = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 
            7:'seven', 8:'eight', 9:'nine'}
#make a dictionary for 10-19
two_place = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
            15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
#make a dictionary for ten places
ten_spots = {20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy',
            80:'eighty', 90:'ninety'}
#take the input number and divide by 10 to find single digit remainder
ones_digits = num_in%10
#take the input number and find the tens place by floor division then multiplication
tens_digits = (num_in//10)*10
#just taking the number directly with the two_digits variable for easier sorting with if statements
two_digits = num_in
#testing my inputs with print functions
print(ones_digits)
print(tens_digits)
print(two_digits)

if tens_digits > 19:
    print(f'The number is written {ten_spots[tens_digits]}-{one_place[ones_digits]}.')
elif two_digits < 20 and two_digits > 10:
    print(f'The number is written {two_place[two_digits]}.')
elif two_digits <10:
    print(f'The number is written {one_place[ones_digits]}')

#Version 2
#handle numbers from 100 - 999
num_in2 = int(input('What number would you like converted to english[100-999]?'))
hundred_spots = {100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred'}
tens_spots_2 = {20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy',
            80:'eighty', 90:'ninety'}
ones_spots_2 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 
            7:'seven', 8:'eight', 9:'nine'}
teens_spots_2 = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
            15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
#take the input number and divide by 10 to find single digit remainder
ones_digits2 = num_in2%10
#take the input number and find the tens place by floor division then multiplication
tens_digits2 = int(str(num_in2)[-2:-1])*10
#just taking the number directly with the two_digits variable for easier sorting with if statements
all_digits = num_in2
hundreds_digits2 = int(str(num_in2)[0:1])*100
#testing my inputs with print functions
print(ones_digits2)
print(tens_digits2)
print(all_digits)
print(hundreds_digits2)
if tens_digits2 > 19:
    print(f'The number is written {hundred_spots[hundreds_digits2]}-{tens_spots_2[tens_digits2]}-{ones_spots_2[ones_digits2]}.')
elif int(str(all_digits)[-2:]) < 20 and int(str(all_digits)[-2:]) > 10:
    print(f'The number is written {hundred_spots[hundreds_digits2]}-{teens_spots_2[int(str(all_digits)[-2:])]}.')
elif int(str(all_digits)[-2:]) <10 and int(str(all_digits)[-2:]) > 0:
    print(f'The number is written {hundred_spots[hundreds_digits2]}-{ones_spots_2[ones_digits2]}')
else :
    print(f'The number is written {hundred_spots[hundreds_digits2]}.')