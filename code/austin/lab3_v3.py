dict1 = {0:'zero', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX',90: 'XC', 100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM', 1000:'M'}
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
            return dict1[tens_dig] + dict1[ones_dig]
    elif num <1000:
        hunds_dig = (num // 100) * 100
        tens_dig = ((num-hunds_dig) // 10) * 10
        ones_dig = num % 10
        under_20 = num - hunds_dig
        if ones_dig == 0:
            if tens_dig == 0:
                return dict1[hunds_dig]
            else:
                return dict1[hunds_dig] + dict1[tens_dig]
        elif tens_dig == 0:
            return dict1[hunds_dig] + dict1[tens_dig]
        elif num - hunds_dig < 20:
            return dict1[hunds_dig] + dict1[under_20]
        else:
            return dict1[hunds_dig]+ dict1[tens_dig] + dict1[ones_dig]
    else:
        return "Input not valid."