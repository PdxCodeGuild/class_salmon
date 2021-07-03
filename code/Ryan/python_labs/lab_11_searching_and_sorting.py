nums = [1, 2, 3, 4, 5, 6, 7, 8]

value = 3

def linear_search(nums, value):
    #print(value)
    for i in range(len(nums)):
        #print(i, nums[i])
        if nums[i] == value:
            output = i
    return output

#index = linear_search(nums, 3)
#print(index)

def binary_search(list, value):
    list.sort()
    i_high = len(list)-1
    num_high = list[-1]
    #print("index high:",i_high, "|number high:", num_high)
    mid = 0 
    i_low = 0
    num_low = list[0]
    #print("index low:", i_low, "|number low:", num_low)
    #print("searching for:", value)
    indexs = [i for i in range(len(nums))]
    #print("search list:", indexs)

    while i_low <= i_high:
        i_mid = (i_high + i_low) // 2
        print("search index:", indexs)
        print("search list :", list)
        print("index high:",i_high, "|number high:", num_high)
        print("index mid:",i_mid, "|number mid:", list[i_mid])
        print("index low:", i_low, "|number low:", num_low)
        print("searching for:", value)


        if list[i_mid] == value:
            print(f"Found {value} at index {i_mid}")
            return
        elif list[i_mid] < value:
            i_low = i_mid + 1
            #print("line 40")
            
        elif list[i_mid] > value:
            #print(list[i_mid])
            #print(i_high)
            #print(i_mid)
            i_high = i_mid - 1
            #print("line 42")
            
        else:
            
            continue

    return print("Value not found")
    

#index = binary_search(nums, 3)

def bubble_sort(nums):

    sorted_nums = []
    for i in range(len(nums)):
        
        sorted_nums.append(nums[i])

        index = len(nums)
        
        for each_element in range(index-1):

            #print(each_element)
        
            for each in range(0, index-each_element-1):
                #print(each)
                #if the element is greater than the next
                if nums[each] > nums[each+1]:
                    # swap the elements
                    nums[each], nums[each+1] = nums[each+1], nums[each]

    print(sorted_nums)

#bubble_sort(nums)