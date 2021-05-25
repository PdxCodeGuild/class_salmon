#implement a linear search
#loop through given list

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


'''while i < 0 in counter:
        print(f'The number {search} is not in the list.')'''
#print(f'The number {search} appears {counter} times in the list.')