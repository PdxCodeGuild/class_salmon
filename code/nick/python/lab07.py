#encryption of the users string input
user_string = input("Please provide a string.")
user_string_lower = user_string.lower()
list_user_string = list(user_string_lower)
print(list_user_string)
ROT13_dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 
'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 
'x':'k', 'y':'l', 'z':'m'}
encoding_string = []
for i in range(len(list_user_string)):
    encoding_string.append(ROT13_dict[list_user_string[i]])
    #remember to put the i in the nested list above.
    print(encoding_string)
#I am not sure this is what the class intent was, but it is my first attempt.


