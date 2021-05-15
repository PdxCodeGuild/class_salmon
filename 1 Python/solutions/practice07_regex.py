
# Practice 6: Regular Expressions



import re


# str1 = 'hello\n\tworld'
# str2 = 'hello\\n\\tworld'
# str3 = r'hello\n\tworld'
# print(str1)
# print(str2)
# print(str3)


# regex = '^(\\d{3})-(\\d{2})-(\\d{4})$'
# regex = r'^(\d{3})-(\d{2})-(\d{4})$'
# result = re.match(regex, '123-45-6789')
# print(result)
# print(result.start()) # 0
# print(result.end()) # 11
# print(result.group()) # 123-45-6789
# print(result.group(1)) # 123
# print(result.group(2)) # 45
# print(result.group(3)) # 6789
# print(result.groups()) # ('123', '45', '6789')
# print(len(result.groups())) # 3

# ss_numbers = result.group(1) + result.group(2) + result.group(3)
# print(ss_numbers)


# result = re.search(r'\d+', 'I went to the store and bought 16 cases of water and it cost $50.')
# print(result.start())
# print(result.end())
# print(result.group())

# result = re.match(r'^\d{3}-\d{3}-\d{4}$', '012-345-67891')
# print(result) # <re.Match object; span=(0, 12), match='012-345-6789'>

# result = re.findall(r'\d+', 'I went to the store and bought 16 cases of water and it cost $50.')
# print(result)

# regex = r'^(\d{3})-(\d{2})-(\d{4})$'
# result = re.findall(regex, '123-45-6789')
# print(result)

# text = '''
# Name,Age
# Bob,67
# Janice,234
# Joanna,4
# '''
# result = re.findall(r'([a-zA-Z]+),(\d+)', text)
# print(result)




# Validate an Email Address
# Write a function `validate_email_address` which returns `True` if the given string is an email address, `False` is it isn't.

def validate_email_address(email):
    regex = r'\w+@\w+\.\w{3}'
    result = re.search(regex, email)
    return result is not None

# print(validate_email_address('test@gmail.com')) # True
# print(validate_email_address('abc123@gmail.com')) # True
# print(validate_email_address('test')) # False
# print(validate_email_address('test@gmail')) # False
# print(validate_email_address('test@gmail@com')) # False


# Validate a Phone Number
# Write a function `validate_phone_number` which returns `True` if the given string is a phone number, `False` if it isn't.

# https://regex101.com/r/lCV6nR/1
def validate_phone_number(phone_number):
    regex = r'^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}'
    result = re.search(regex, phone_number)
    return result is not None
# print(validate_phone_number('0123456789')) # True
# print(validate_phone_number('012-345-6789')) # True
# print(validate_phone_number('(012) 345-6789')) # True
# print(validate_phone_number('012-3A5-6789')) # False
# print(validate_phone_number('1-1-1')) # False


# Clean a Phone Number
# Write a function `clean_phone_number` which returns a string containing just the numbers of a phone number if it's valid, `None` if it's not. Hint: use capture groups.

def clean_phone_number(phone_number):
    regex = r'^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})'
    result = re.search(regex, phone_number)
    if result is None:
        return None
    # return ''.join(result.groups())
    return result.group(1) + result.group(2) + result.group(3)
    # return ''.join(result.groups()) if result is not None else None
    
# print(clean_phone_number('0123456789')) # 0123456789
# print(clean_phone_number('012-345-6789')) # 0123456789
# print(clean_phone_number('(012) 345-6789')) # 0123456789
# print(clean_phone_number('012-3A5-6789')) # None
# print(clean_phone_number('1-1-1')) # None

# Find All Numbers
# Write a function `find_numbers` which returns a list of floats found in the given string.

def find_numbers(text):
    regex = r'-?\d+\.\d+'
    nums = re.findall(regex, text)
    # print(nums) # ['1.23', '5.45', '-1.34', '43.123']
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    return nums

text = '''
name  favorite number
joe   1.23
jane  5.45
julie -1.34
bob   43.123
'''
print(find_numbers(text)) # [1.23, 5.45, -1.34, 43.123]











