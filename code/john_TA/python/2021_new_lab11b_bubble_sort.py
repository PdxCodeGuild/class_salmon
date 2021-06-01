nums = [5, 4, 3, 9, 1, 4, 0, 8, 4, 99, ]
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, ]
print(nums)

def bubble_sort(nums):
    for iteration in range(len(nums)-1): # len-1 works, but i can't 100% understand why. because each swap will take care of the ends automatically? so a len=3 would require only one pass with two comparisons?
        for i in range(len(nums)):
            try:
                if nums[i] > nums[i+1]:
                    # print(f'nums[i]={nums[i]} > nums[i+1]={nums[i+1]}')
                    temp_num_greater = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp_num_greater
            except: pass  # unnecessary, but one way to make this a "more efficient" bubble sort, oxymoronic as that is!
        print(nums)
        print(f'~~~~~~~~end while loop, iteration={iteration}')
    return nums

bubble_sort(nums)
print('~~~~~~~~~~~~~~~~~end~~~')
