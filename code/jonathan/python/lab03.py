def numbers_to_words(y):
    x = input("Give me a number between 0 and 999 please: ")
    x = int(x)
    hundreds_digit = x//100
    tens_digit = x//10%10
    ones_digit = x%10

    english_phrase = ""

    if x >= 100:
        # takes the digit and finds the correct key from the dictionary
        hundreds = numbers_to_words_hundreds[hundreds_digit]
        # if the second digit is a zero
        if tens_digit == 0:
            # if the ones digit is not a zero
            if ones_digit > 0:
                # takes the digit and finds the correct key from the dictionary
                ones = numbers_to_words_ones[ones_digit]
                # prints the hundreds and ones as words since we don't say the middle zero in English
                english_phrase = (f"{hundreds} and {ones}.")
                return english_phrase
            # this is for any case the tens and ones digit are zeros
            else: 
                # if the tens and ones digits are zeros we only need to print the hundreds
                english_phrase = (f"{hundreds}.")
                return english_phrase
        # if the tens digit is greater than zero 
        if tens_digit >=1 and ones_digit == 0:
            # takes the digit and finds the correct key from the dictionary
            tens = numbers_to_words_tens[tens_digit]
            # prints the hundreds, tens, and ones digits adding in "and" and "-"
            english_phrase = (f"{hundreds} and {tens}.")
            return english_phrase
        if tens_digit >=1:
            # takes the digit and finds the correct key from the dictionary
            tens = numbers_to_words_ten_hun[tens_digit]
            # takes the digit and finds the correct key from the dictionary
            ones = numbers_to_words_ones[ones_digit]
            # prints the hundreds, tens, and ones digits adding in "and" and "-"
            english_phrase = (f"{hundreds} and {tens}-{ones}.")
            return english_phrase
    # for numbers only having a tens and ones digit
    if x < 100:
        # if the input is between 20 and 99
        if tens_digit >= 2: 
            # takes the digit and finds the correct key from the dictionary
            tens = numbers_to_words_tens[tens_digit]
            # if the ones digit is greater than zero
            if ones_digit > 0:
                # takes the digit and finds the correct key from the dictionary
                ones = numbers_to_words_ones[ones_digit]
                # print out both tens and ones digit
                english_phrase = (f"{tens}-{ones}.")
                return english_phrase
            # if the number ends in a zero    
            else: 
                # only thing left is if ones digit is a zero will only need to print the tens digit
                english_phrase = (f"{tens}.")
                return english_phrase
        # if the input is between 10 and 19
        if tens_digit == 1: 
            # refers to outliers dictionary due to English language rules
            outliers = numbers_to_words_outliers[ones_digit]
            # prints directly from the dictionary
            english_phrase = (f"{outliers}.")
            return english_phrase
    # if the input is below 10            
    if x < 10: 
        # takes the digit and finds the correct key from the dictionary
        ones = numbers_to_words_ones[ones_digit] 
        # needs to only print the ones digit
        english_phrase = (f"{ones}.")
        return english_phrase

def numbers_to_numerals(y):
    '''Takes the user input of a number between 0 
       and 999 and convert it into Roman Numerals
    '''
    # user will input a number
    x = input("Give me a number between 0 and 999 please: ")
    # cast string into an integer to manipulate 
    x = int(x)

    english_phrase = ""

    # outputs the hundreds digit
    hundreds_digit = x//100
    # outputs the tens digit
    tens_digit = x//10%10
    # outputs the ones digit
    ones_digit = x%10
    
    # for numbers 100 to 999
    if x >= 100:
        # retrieves the hundreds digit from the dictionary
        hundreds = roman_numerals_hundreds[hundreds_digit]
        # for cases where the tens digit is zero
        if tens_digit == 0:
            # if the ones digit is anything but zero
            if ones_digit >= 1:
                # retrieves the ones digit from the dictionary
                ones = roman_numerals_ones[ones_digit]
                # no need to output zero's in roman numerals
                english_phrase = (f"{hundreds}{ones}.")
                return english_phrase
            else: # when tens and ones are zeros 
                english_phrase = (f"{hundreds}.")
                return english_phrase
        # for cases when the tens digit is anything but zero
        if tens_digit >=1: 
            # if the ones digit equals zero
            if ones_digit == 0:
                # do not need to output the tens digit when zero
                tens = roman_numerals_tens[tens_digit]
                english_phrase = (f"{hundreds}{tens}.")
                return english_phrase
            else: # for when the tens and ones are not zero
                # retrieves the tens digit from the dictionary
                tens = roman_numerals_tens[tens_digit]
                # retrieves the ones digit from the dictionary
                ones = roman_numerals_ones[ones_digit]
                english_phrase = (f"{hundreds}{tens}{ones}.")
                return english_phrase
    # for cases when the input is less than 100
    # for cases when the input is less than 10
    if x < 10: 
        # retrieves the ones digit from the dictionary
        ones = roman_numerals_ones[ones_digit]
        english_phrase = (f"{ones}.")
        return english_phrase
    if x < 100:
        # retrieves the tens digit from the dictionary
        tens = roman_numerals_tens[tens_digit]
        # for cases when the ones digit is not zero
        if ones_digit >= 1:
                # retrieves the ones digit from the dictionary
                ones = roman_numerals_ones[ones_digit]
                english_phrase = (f"{tens}{ones}")
                return english_phrase
        else: # if the number ends in a zero no need to print the ones digit
                english_phrase = (f"{tens}.")
                return english_phrase

def numbers_to_time(y):
    # ask the user for a time in 12 hour format with a colon
    time = input("Give me the time please (12h hh:mm): ")
    # asking for am or pm
    go = input("am or pm: ")

    english_phrase = ""

    # removes the colon from the input to enable it to cast into an integer later
    number_time = time.replace(':', '')
    
    # for when the time is exactly 12
    if number_time == "1200":
        if go == "am":
            english_phrase = ("It is midnight.")
            return english_phrase
        else:
            english_phrase = ("It is noon.")
            return english_phrase

    # for when the time is 10-12 o'clock
    elif len(number_time) == 4:
        # cast to integer to allow math to be performed
        number_time = int(number_time)    
        # returns a two digit number for the hour
        hours_two_digit = number_time//100
        # determines which time of day suffix to add
        if go == "pm":
            toki = time_of_day_pm[hours_two_digit]
        else:
            toki = time_of_day_am[hours_two_digit]
        # retrieves the number from the dictionary giving us the hour in two digits
        hour = time_hours[hours_two_digit]
        # returns a one digit number for the tens digit in the minutes
        minutes_tens_digit = number_time//10%10
        # returns a one digit number for the ones digit in the minutes
        minutes_ones_digit = number_time%10
        # if the minutes in the tens place are 1-9
        if minutes_tens_digit > 0:
            # takes the digit and finds the correct key from the dictionary
            tens_minutes = minutes_tens[minutes_tens_digit]
            # if the minutes in the ones place are 1-9
            if minutes_ones_digit > 0:
                # takes the digit and finds the correct key from the dictionary
                ones_minutes = minutes_ones[minutes_ones_digit]
                # prints the hundreds tens and ones as words
                english_phrase = (f"It is {tens_minutes}-{ones_minutes} minutes after {hour}{toki}.")
                return english_phrase
            else:
                english_phrase = (f"It is {tens_minutes} minutes after {hour}{toki}.")
                return english_phrase
        elif minutes_tens_digit == 0:
            # if the ones digit is not a zero
            minutes_ones_digit = number_time%10
            if minutes_ones_digit > 0:
                # takes the digit from line 54 and finds the correct key from the dictionary
                ones_minutes = minutes_ones[minutes_ones_digit]
                # prints the hundreds and ones as words since we don't say the middle zero in English
                english_phrase = (f"It is {ones_minutes} minutes after {hour}{toki}.")
                return english_phrase
        else: # for when the time is between 10-12 on the dot
            english_phrase = (f"It is {hour}{toki}.")
            return english_phrase
    else:
        # cast to integer to allow math to be performed
        number_time = int(number_time)
        # returns a one digit number for the hour
        hours_one_digit = number_time//100
        # determines which time of day suffix to add
        if go == "pm":
            toki = time_of_day_pm[hours_one_digit]
        else:
            toki = time_of_day_am[hours_one_digit]
        # retrieves the number from the dictionary giving us the hour
        hour = time_hours[hours_one_digit]
        # returns the minutes ten digit as a single number
        minutes_tens_digit = number_time//10%10
        # returns the minutes one digit as a single number
        minutes_ones_digit = number_time%10
        # for when the time is between 1-9 AND the minutes are 00
        if minutes_ones_digit == 0 and minutes_tens_digit == 0:
            english_phrase = (f"It is {hour}{toki}.")
            return english_phrase
        if minutes_tens_digit == 0:
            # if the ones digit is not a zero
            minutes_ones_digit = number_time%10
            if minutes_ones_digit > 0:
                # takes the digit from line 54 and finds the correct key from the dictionary
                ones_minutes = minutes_ones[minutes_ones_digit]
                # prints the ones minutes, hour, and time of day
                english_phrase = (f"It is {ones_minutes} minutes after {hour}{toki}.")
                return english_phrase
        # returns the minutes one digit as a single number
        minutes_ones_digit = number_time%10
        if minutes_tens_digit >=1:
            # takes the digit and finds the correct key from the dictionary
            tens_minutes = minutes_tens[minutes_tens_digit]
            # takes the digit and finds the correct key from the dictionary
            ones_minutes = minutes_ones[minutes_ones_digit]
            # prints the tens and ones minutes, and hour and time of day
            english_phrase = (f"It is {tens_minutes}-{ones_minutes} minutes after {hour}{toki}.")
            return english_phrase

# the outliers for the numbers to words portion because of English
numbers_to_words_outliers = {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}
numbers_to_words_t = {
    1: "ten"
}
# the ones digit for the numbers to words portion
numbers_to_words_ones = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
# the tens digit for the numbers to words portion for numbers over 100
numbers_to_words_ten_hun = {
    1: "teen",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}
# the tens digit for the numbers to words portion
numbers_to_words_tens = {
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}
# the hundreds digit for the numbers to words portion
numbers_to_words_hundreds = {
    1: "one hundred",
    2: "two hundred",
    3: "three hundred",
    4: "four hundred",
    5: "five hundred",
    6: "six hundred",
    7: "seven hundred",
    8: "eight hundred",
    9: "nine hundred"
}
# the ones digit for the numbers to Roman Numerals
roman_numerals_ones = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX"
}
# the tens digit for the numbers to Roman Numerals
roman_numerals_tens = {
    1: "X",
    2: "XX",
    3: "XXX",
    4: "XL",
    5: "L",
    6: "LX",
    7: "LXX",
    8: "LXXX",
    9: "XC"
}
# the hundreds digit for the numbers to Roman Numerals
roman_numerals_hundreds = {
    1: "C",
    2: "CC",
    3: "CCC",
    4: "CD",
    5: "D",
    6: "DC",
    7: "DCC",
    8: "DCCC",
    9: "CM"
}  
# the hours digit for the numbers to time
time_hours = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve"
}
# the tens digit for the numbers to time
minutes_tens = {
    1: "teen",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty"
}
# the minute digit for the numbers to time
minutes_ones = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
} 
# time of day am suffix
time_of_day_am = {
    1: " in the morning", 
    2: " in the morning",
    3: " in the morning",
    4: " in the morning",
    5: " in the morning",
    6: " in the morning",
    7: " in the morning",
    8: " in the morning",
    9: " in the morning",
    10: " in the morning",
    11: " in the morning"
}
# time of day pm suffix
time_of_day_pm = {
    1: " in the afternoon",
    2: " in the afternoon",
    3: " in the afternoon",
    4: " in the afternoon",
    5: " in the afternoon",
    6: " in the evening",
    7: " in the evening",
    8: " in the evening",
    9: " in the evening",
    10: " at night",
    11: " at night",
    12: " at night"
}

# ask the user a choice, store their response in a variable
# the program will break if the user inputs anything outside of these three options
y = input("Choose between numbers, roman numerals, or time please: ")

# chooses which function to run based off of the user answer
if y == "numbers":
    print(numbers_to_words(y))
if y == "roman numerals":
    print(numbers_to_numerals(y))
if y == "time":
    print(numbers_to_time(y))