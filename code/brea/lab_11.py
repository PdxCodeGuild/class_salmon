def search(x,val):
    for i, value in enumerate(x):
        if val == value:
            return i
    return 'value not found'

# nums = [13,98,75,25,41,63]
# x = search(nums, 75) 


def BinarySearch(x,key):
    x.sort()
    low = 0
    high = len(x) - 1
    found = False
    while low <= high and found == False:
        mid = (low+high)//2
        if key == x[mid]:
            found = True
        elif key < x[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if found == True:
        return mid
    else:
        return 'not found'

# nums = [13,98,75,25,41,63]
# y = BinarySearch(nums,75)


def BubbleSort(y):
    index = len(y) -1 
    list_sorted = False
    while not list_sorted:
        list_sorted = True
        for x in range(len(y)-1):
            if y[x] > y[x+1]:
                list_sorted = False
                y[x], y[x+1] = y[x+1], y[x]
    return y

print(BubbleSort([1,25,78,54]))    