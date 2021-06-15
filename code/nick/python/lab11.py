#implement a linear search
#loop through given list
import math
search = input('What number are you looking for (0-9)?') #0 and 9 should return nothing, 5 return 6 here
list = [1, 2, 3, 4, 5,5, 5,5,5,5, 6, 7, 8]

def linear_search(list, search):
    counter = 0
    for i in list:
        #search needs to be converted to an integer because it is a string input at the beginning
        if i == int(search):
            counter += 1
    return counter
print(f'The number {search} appears {linear_search(list,search)} times in the list.')
#pseudocode of the binary function from wiki
'''function binary_search_alternative(A, n, T) is
    L := 0
    R := n − 1
    while L != R do
        m := ceil((L + R) / 2)
        if A[m] > T then
            R := m − 1
        else:
            L := m
    if A[L] = T then
        return L
    return unsuccessful''' 
#create an array (A) of elements (n)
A = [2,5,6,7,8,3,1,4,0,9]#this list has 10 items
A.sort()
#n is equivalent to the number of elements in the list above
n = len(A)
#check the length of the list with print function
#print(n)
#T is the target value of the binary search, according to wiki
#I guess this means we cannot have duplicates in A?
T = int(input('pick a number to search for in the binary search algo: '))
def binary_search(A, n, T):
    low = 0
    print(low)
    high = n - 1
    #print(high)
    while low != high:
        #m is the position of the middle element. When this = T we are good
        m = math.ceil((low + high)/2)
        #print(A[m])
        if A[m] > T:
            high = m - 1
        else:
            low = m    
    if A[low] == T:
        return (f'The target number is at index {A[low]}.')
    else:
        return ('unsuccessful')
print(binary_search(A,n,T))

#Part 3 Bubble Sort
'''procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat #while some condition not met while == True: break
        swapped = false
        for i := 1 to n - 1 inclusive do
            /* if this pair is out of order */
            if A[i - 1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i - 1], A[i])
                swapped := true
            end if
        end for
    until not swapped #starts at the repeat
end procedure'''
#pseudocode for bubble sort
#the point of the algorithm is to sort out an unsorted list
#make an unsorted list
b = [5,3,7,8,1,2,0,4]

def bubble_sort(b):
    n = len(b)
    #so we know the number of elements n and we want to check index in range of all elements minus one
    for iteration in range(n-1):#so this is running a bunch of times through the list or it is meant to
        #??? make a marker, I guess
        marker = 0 #this starts as zero then it goes up to one if the for loop sorts the list correctly.
        for x in range(n-1):#range(start, stop[, step]) I tried this for the whole length n-1 but it does not work
            #print(x)
            #print(marker)
            if b[x] > b[x+1]: #the index(another index?)
                #swap them and remember something changed
                #to do this I think we store the value at the small position, bigger value
                store_bigger_value = b[x]
                #print(b)
                #print(b[i])
                #print(b[i+1])
                store_small_value = b[x+1]
                #now the big value can take the small value position
                b[x+1] = store_bigger_value
                #now the small value in store can be assigned to the ...
                b[x] = store_small_value
                marker = 1 #I tried doing this += beforehand and it does not work, the point is that the i position either is sorted correctly or is not.
                #it does not make sense to use a counter here.
            #else:
            #    break
        if marker == 1:#
            return bubble_sort(b)
    #print(b)
    return b             
        #I think this will compare the length in marker to the length in the now sorted list
        #when they are the same the for loop should exit then return b
        #if marker == range(n-1): #this does not work
        #    break
        #return b
print(bubble_sort(b))
print(b)
#This appears to be working now