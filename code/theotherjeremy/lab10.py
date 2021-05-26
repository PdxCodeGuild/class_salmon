def linear_search(nums, value):
    return nums.index(value)


nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 5)


def binary_search(list, target):
    my_list = list[:]
    my_list.sort()
    low = my_list[0]
    high = my_list[-1]
    while low < high:
        x = int((my_list[high] + my_list[low])/2)
        print(x)
        mid = my_list[x]
        if mid == target:
            print(f'The {target} is at index {mylist[mid]}')
            break
        else:
            if target > mid:
                low = mid
            elif target < mid:
                high = mid


print(binary_search(nums, 3))
