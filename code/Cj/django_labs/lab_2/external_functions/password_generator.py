import random # Random imported
import string
# Input = int(input('how many characters do you want your password to be? ')) #input from user converted to integer and assigned to variable 
# Input2 = int(input('how many letters do you want it to have? '))
# data = 0
# output = ''
# while Input2 > Input:
#     print(f' {Input2} is larger than {Input} please pick a smaller number ')
#     Input2 = int(input('how many letters do you want it to have? '))
# data = int(input('how many special characters do you want? '))
# while data > Input - Input2:
#     print(f' {data} + {Input2} = a password length of {data + Input2} which is larger than your total password size of {Input} please enter a smaller number. ')
#     data = int(input('how many special characters do you want? '))
# for each in range(Input2):
#     var = (random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')) # Random choice assigned to variable
#     output += var
# for each in range(data):
#     var = (random.choice('!@#$%^&*()_'))
#     output += var
# Input3 = Input - (Input2 + data)
# for each in range(Input3):
#     var = (random.choice('1234567890'))
#     output += var
# output = list(output)
# random.shuffle(output)
# output = ''.join(output)

# print(output)



    




# Input3 = int(input('how many numbers do you want it to have? '))
# output ='' # output variable established

# for each in range(Input2): # for loop established with the range = input
#     var = random.choice('abcdefghijklmnopqrstuvwxyz') # Random choice assigned to variable
#     output += str(var)  # variable concatenated into output.
# for each in range(Input3):
#     var = random.choice('1234567890')  
#     output += str(var) 



# print(f' Your password is {output}') # output statement with variable


# print(string.ascii_letters)
def shorten():
    short_url = []
    for i in range(5):
        short_url += random.choice(string.ascii_letters)
    num = str(random.randint(0, 9))
    index = random.randint(0, 4)
    short_url[index] = num
    output = ''
    for i in short_url:
        output += i
    return output

link = shorten()
print(link)



