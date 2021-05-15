



# def make_change():
#     amount = float(input('what is the amount? '))
#     ...
#     print('You have x quarters')
# make_change()


def make_change(amount):
    amount = int(amount * 100)
    quarters = amount // 25
    amount -= quarters*25 # amount %= 25
    dimes = amount // 10
    amount -= dimes * 10
    nickles = amount // 5
    amount -= nickles * 5
    pennies = amount

    return quarters, dimes, nickles, pennies




def pluralize(value, singular_noun):
    # if value is not equal to 1
    if value != 1:
        # if text ends in 'y', append an 'ies'
        if singular_noun.endswith('y'):
            return singular_noun.replace('y', 'ies')
        # if text ends in anything other than 'y', append an 's'
        else:
            return singular_noun + 's'
    # if the value is equal to one
        # return the singular noun
    else:
        return singular_noun

# print(pluralize(1, 'dime')) # 'dime'
# print(pluralize(2, 'dime')) # 'dimes'
# print(pluralize(1, 'penny')) # 'penny'
# print(pluralize(2, 'penny')) # 'pennies'
# exit()

def make_change_v2(amount, coin_values):
    amount = int(amount * 100)
    output = []
    for coin_value in coin_values:
        name, value = coin_value # unpack the tuple representing the coin ('dime', 10) into two separate variables
        coin_count = amount // value # calculate the coin count
        amount -= coin_count * value # update the amount
        output.append((name, coin_count)) # adding a tuple containing the coin name and count to our output
    return output
    


if __name__ == '__main__':
    # amount = float(input('what is the amount? '))
    # quarters, dimes, nickles, pennies = make_change(amount)
    # print(f'Your change is {quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies')


    coin_values = [
        ('half-dollar', 50),
        ('quarter', 25),
        ('dime', 10),
        ('nickel', 5),
        ('penny', 1)
    ]
    amount = float(input('what is the amount? '))
    # example output [('half-dollar', 2), ('quarter', 1), ('dime', 1), ('nickel', 0), ('penny', 1)]
    coin_amounts = make_change_v2(amount, coin_values)
    output_strings = []
    for coin_amount in coin_amounts: # iterate over the coins
        name, count = coin_amount # unpack the tuple into individual variables
        if count > 0:
            output_strings.append(str(count) + ' ' + pluralize(count, name))
    print('Your change is: ' + ', '.join(output_strings)) # avoid the trailing comma problem


