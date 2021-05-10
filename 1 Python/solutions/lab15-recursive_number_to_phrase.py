ONES = dict(zip(range(10), ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))
TENS = dict(zip(range(10), ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']))
TEENS = dict(zip(range(10, 20), ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']))
illions = zip([10**zeros for zeros in range(6, 34, 3)], [prefix+'illion' for prefix in ['m', 'b', 'tr', 'quadr', 'quint', 'sext', 'sept', 'oct', 'non', 'dec']])
ILLIONS = dict(reversed(list(illions)))

def number_to_phrase(num):
    """
    recursively generates number to phrase
    """
    original_num = num
    prefix = []
    phrase = []

    if num > 10**36:
        return 'Invalid number. Enter number between 0 and 999 decillion.'

    # recursively add x-illion to prefix
    for illion in ILLIONS:
        if num >= illion:
            illion_prefix = number_to_phrase(num // illion)
            prefix.append(f'{illion_prefix} {ILLIONS[illion]}')
            num = num % illion

    # recursively add thousands to prefix
    if num > 999:
        thousand_prefix = number_to_phrase(num // 1000)
        prefix.append(f'{thousand_prefix} thousand')
        num = num % 1000

    # calculate hundreds
    if num >= 100:
        hundreds_digit = num % 1000 // 100
        phrase.append(f'{ONES[hundreds_digit]} hundred')
    
    tens_digit = num % 100 // 10
    ones_digit = num % 10
    # calculate tens
    if tens_digit > 1:
        tens = TENS[tens_digit]
        if tens_digit and ones_digit:
            ones = ONES[ones_digit]
            phrase.append(tens+'-'+ones)
        else:
            phrase.append(tens)

    # calculate teens
    elif tens_digit == 1:
        teen = num % 100
        phrase.append(TEENS[teen])

    # calculate ones
    else:
        if original_num == 0:
            return 'zero'
        phrase.append(ONES[ones_digit])

    return ' '.join(prefix + phrase)


def main():
    while True:
        user_in = input("Enter a number to convert it to English, or 'x' to exit: ").strip()
        if user_in in ['x', 'exit']:
            break
        try:
            num = int(user_in.replace(',',''))
            print(number_to_phrase(num))
        except ValueError:
            print('Error: Invalid number')
main()
