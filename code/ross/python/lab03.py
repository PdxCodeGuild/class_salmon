print("""
This program can do one of three things:
\t* convert a number into it's English word(s)
\t* convert a number into Roman numerals
\t* or convert a time into English.
""")

print("Which function would you like to perform?")

choice = input("""
\tPress (1) for number to English. 
\tPress (2) for number to Roman numerals.
\tPress (3) for time into English.
\nInput your choice here: """)

num = 0
english_ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
english_tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
english_hundreds = {1: "one-hundred", 2: "two-hundred", 3: "three-hundred", 4: "four-hundred", 5: "five-hundred", 6: "six-hundred", 7: "seven-hundred", 8: "eight-hundred", 9: "nine-hundred"}
roman_ones = {0: 'nulla (there is no zero in Roman numerals)', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
roman_tens = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXX', 9: 'XC'}
roman_hundreds = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}

def over_hundred(hundreds_digit, tens_digit, ones_digit, num):
    tens_digit %= 10
    if ones_digit == 0:
        if tens_digit == 1:
            print(english_hundreds[hundreds_digit], "ten")
        else:
            print(english_hundreds[hundreds_digit], english_tens[tens_digit])
    elif tens_digit == 1:
        print(english_hundreds[hundreds_digit], teens[num%100])
    else:
       print(english_hundreds[hundreds_digit], english_tens[tens_digit], english_ones[ones_digit])

def roman_over_hundred(hundreds_digit, tens_digit, ones_digit, num):
    tens_digit %= 10
    if ones_digit == 0:
        if tens_digit == 1:
            print(roman_hundreds[hundreds_digit], "X")
        else:
            print(roman_hundreds[hundreds_digit], roman_tens[tens_digit])
    else:
       print(roman_hundreds[hundreds_digit], roman_tens[tens_digit], roman_ones[ones_digit])

if choice == '1': # this if runs if user picks to convert to English
    num = int(input("\nInput a number to convert to it's English form: "))
    hundreds_digit = num // 100
    tens_digit = num // 10
    ones_digit = num % 10
    if num >= 0 and num < 10:
        print(english_ones[ones_digit])
    elif num >= 10 and num <20:
        print(teens[num])
    elif num >= 20 and num < 100:
        if ones_digit == 0:
            print(english_tens[tens_digit])
        else:
            print(english_tens[tens_digit], "-", english_ones[ones_digit])
    elif num >= 100:
        over_hundred(hundreds_digit, tens_digit, ones_digit, num)
    else:
        print("Sorry please input a number between 0 and 999.")
elif choice == '2': # this if runs if users chooses to convert to Roman numerals
    num = int(input("\nInput a number to convert to it's Roman numeral form: "))
    hundreds_digit = num // 100
    tens_digit = num // 10
    ones_digit = num % 10
    if num >= 0 and num < 10:
        print(roman_ones[ones_digit])
    elif num >= 10 and num < 100:
        if ones_digit == 0:
            print(roman_tens[tens_digit])
        else:
            print(roman_tens[tens_digit], roman_ones[ones_digit])
    elif num >= 100:
        roman_over_hundred(hundreds_digit, tens_digit, ones_digit, num)
    else:
        print("Sorry please input a number between 0 and 999.")
elif choice == '3': # this if runs if user chooses to convert a time
    user_time = input("\nPlease enter the current time in 24-hour format (example, 0430/04:30 for 4:30am or 1630/16:30 for 4:30pm): ")
    time = int(user_time.replace(':', ''))
    output_time = []
    hours = time // 100
    minutes = time % 100
    if hours == 0:
        output_time.append("zero zero")
    elif hours > 0 and hours < 10:
        output_time.append(english_ones[hours])
    elif hours >= 10 and hours < 20:
        output_time.append(teens[hours])
    elif hours >= 20:
        output_time.append("twenty")
        output_time.append(english_ones[hours % 20])
    if minutes == 0:
        output_time.append("zero zero")
    elif minutes > 0 and minutes < 10:
        if minutes // 10 == 0:
            output_time.append("zero")
            output_time.append(english_ones[minutes])
        else:
            output_time.append(english_tens[minutes // 10])
            output_time.append(english_ones[minutes % 10])
    elif minutes >= 10 and minutes < 20:
        output_time.append(teens[minutes])
    elif minutes >= 20 and minutes <= 60:
        if minutes % 10 == 0:
            output_time.append(english_tens[minutes // 10])
        else:
            output_time.append(english_tens[minutes // 10])
            output_time.append(english_ones[minutes % 10])
    print(f"The current time is {'-'.join(output_time)} which you entered as {user_time}")
else: # if the user chooses an invalid input, this runs
    print("\nSorry please try again with a 1, 2, or 3.\n")