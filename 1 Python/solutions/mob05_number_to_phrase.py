# dictionaries for looking up english word corresponding with the number
# because there is no discernable pattern 1-19 we had to hardcode them in a dictionary
less_19_dic = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen"
    
}
over_19_dic  = {
    2 : "twenty",
    3 : "thirty",
    4 : "fourty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety"
}
# this function takes a number and converts it to its written form
def number_to_word(num):
    # if the number is less than 20 it will be pulled from a hardcoded dictionary
    if num < 20:
        output= less_19_dic[num]
        return output
    elif num < 100: 
        # Break the number into its ones digit and tens digit
        ones_digit = num % 10
        tens_digit = num // 10
        # if the ones digit is 0 just print the tens digit
        # avoiding returning 'twenty-zero' 
        if ones_digit == 0:
            output = over_19_dic[tens_digit]
        else:
            output = over_19_dic[tens_digit] + "-" + less_19_dic[ones_digit]
        return output
    elif num < 1000:
        ones_digit = num % 10
        tens_digit = (num // 10)%10
        hundreds_digit = num//100
        # print(hundreds_digit,tens_digit,ones_digit)
        if tens_digit < 2:
            key = 10*tens_digit+ones_digit
            if key == 0:
                output = less_19_dic[hundreds_digit] + " hundred"
            else:
                output = less_19_dic[hundreds_digit] + " hundred and " + less_19_dic[key]
        else:
            if ones_digit == 0:
                output =less_19_dic[hundreds_digit]+ " hundred and "+ over_19_dic[tens_digit]
            else:
                output =less_19_dic[hundreds_digit]+ " hundred and "+ over_19_dic[tens_digit] + "-" + less_19_dic[ones_digit]
            #output = less_19_dic[hundreds_digit]+ " hundred and " +over_19_dic[tens_digit] + "-" + less_19_dic[ones_digit]
        return output
    else:
        print("Number not supported!")
        return None
# testing our function
for i in range(1000):
    print(i, number_to_word(i))
# print(number_to_word(516))