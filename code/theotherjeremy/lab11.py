'''def linear_search(nums, value):
    return nums.index(value)


index = linear_search(nums, 5)
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8]


def binary_search(list, target):
    my_list = list[:]
    my_list.sort()
    low_val = my_list[0]
    high_val = my_list[-1]

    while low_val < high_val:
        x = int((my_list.index(high_val) + my_list.index(low_val))//2)
        print(x)
        mid = my_list[x]
        if mid == target:
            print(f'The {target} is at index {my_list[mid]}')
            break
        else:
            if target > mid:
                low_val = mid
            elif target < mid:
                high_val = mid


'''

    '''

print(binary_search(nums, 3))
