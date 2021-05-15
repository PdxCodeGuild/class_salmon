



fruits = ['apples', 'bananas', 'pears']
print(fruits)
# iterating over the elements of a list
for fruit in fruits:
    print(fruit)
    fruit += '!'
    print(fruit)
print(fruits)

# iterate over the indices of a list
for i in range(len(fruits)):
    # print(fruits[i])
    fruits[i] += '!'
print(fruits)



def validate_credit_card(credit_card):

    print(credit_card)
    # '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'

    # Convert the input string into a list of ints
    credit_card = credit_card.split(' ')
    
    print(credit_card)
    # ['4', '5', '5', '6', '7', '3', '7', '5', '8', '6', '8', '9', '9', '8', '5', '5']
    
    for i in range(len(credit_card)): # i will go 0 1 2 3 ... 15
        credit_card[i] = int(credit_card[i]) # use the index to access the element
    
    # cc2 = []
    # # for i in range(len(credit_card)):
    # #     cc2.append(int(credit_card[i]))
    # for num in credit_card: # iterate over the elements of our list
    #     cc2.append(int(num)) # convert the element to an int and append it to the new list
    # credit_card = cc2 # replace original list with the new list

    print(credit_card)
    # [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

    # Slice off the last digit. That is the check digit.

    check_digit = credit_card.pop()
    print(credit_card)
    # [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5]

    # Reverse the digits.

    credit_card.reverse()

    print(credit_card)
    # [5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4]

    # Double every other element in the reversed list.
    for i in range(0, len(credit_card), 2):
        # print(i, credit_card[i])
        # credit_card[i] = credit_card[i]*2
        credit_card[i] *= 2
    
    print(credit_card)
    # [10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]

    # Subtract nine from numbers over nine.
    for i in range(len(credit_card)):
        if credit_card[i] > 9:
            credit_card[i] -= 9
    
    print(credit_card)
    # [1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]

    # Sum all values.
    total = sum(credit_card)
    print(total) # 85

    # Take the second digit of that sum.
    second_digit = total % 10

    # If that matches the check digit, the whole card number is valid.
    # return second_digit == check_digit
    if second_digit == check_digit:
        return True
    else:
        return False


credit_card = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
print(validate_credit_card(credit_card)) # True

credit_card = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 4'
print(validate_credit_card(credit_card)) # False


