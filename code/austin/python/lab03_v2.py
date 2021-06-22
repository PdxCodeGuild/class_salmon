dict1 = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty',90: 'ninety', 100:'one hundred', 200:'two hundred', 300:'three hundred', 400:'four hundred', 500:'five hundred', 600:'six hundred', 700:'seven hundred', 800:'eight hundred', 900:'nine hundred'}
def num_to_words(num):
    ones_dig = 0
    tens_dig = 0
    hunds_dig = 0
    if num <20:
        return dict1[num]
    elif num <100:
        tens_dig = (num // 10) * 10
        ones_dig = num % 10
        if ones_dig == 0:
            return dict1[tens_dig]
        else:
            return dict1[tens_dig] + '-' + dict1[ones_dig]
    elif num <1000:
        hunds_dig = (num // 100) * 100
        tens_dig = ((num-hunds_dig) // 10) * 10
        ones_dig = num % 10
        under_20 = num - hunds_dig
        if num - hunds_dig < 20 and ones_dig != 0:
            return dict1[hunds_dig] + ' and ' + dict1[under_20]
        elif ones_dig == 0:
            if tens_dig == 0:
                return dict1[hunds_dig]
            else:
                return dict1[hunds_dig] + ' and ' + dict1[tens_dig]
        elif tens_dig == 0:
            return dict1[hunds_dig] + ' and ' + dict1[tens_dig]
        else:
            return dict1[hunds_dig]+ ' and ' + dict1[tens_dig] + '-' + dict1[ones_dig]
    else:
        return "Input not valid."

for num in range(0,1000):
    print(num_to_words(num))