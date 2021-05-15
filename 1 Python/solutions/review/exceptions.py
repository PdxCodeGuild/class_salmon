
def get_int():
    value = ''
    while True:
        try:
            value = input('enter an integer: ')
            value = int(value)
            break
        except ValueError:
            print('that is not a valid integer')
    return value

print(get_int())

def find_number(nums, target):
    for num in nums:
        if num == target:
            print('found it!')
            break
    else:
        print('could not find the number')


find_number([45, 56, 67], 89)
