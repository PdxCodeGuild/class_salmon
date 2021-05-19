num = int(input("Input a number to convert to it's English form: "))
english_ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
english_tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
english_hundreds = {1: "one-hundred", 2: "two-hundred", 3: "three-hundred", 4: "four-hundred", 5: "five-hundred", 6: "six-hundred", 7: "seven-hundred", 8: "eight-hundred", 9: "nine-hundred"}
hundreds_digit = num // 100
tens_digit = num // 10
ones_digit = num % 10

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


if num >= 0 and num < 10:
    print(english_ones[ones_digit])
elif num >= 10 and num <20:
    print(teens[num])
elif num >= 20 and num < 100:
    print(english_tens[tens_digit], "-", english_ones[ones_digit])
elif num >= 100:
    over_hundred(hundreds_digit, tens_digit, ones_digit, num)
else:
    print("Sorry please input a number between 0 and 999.")