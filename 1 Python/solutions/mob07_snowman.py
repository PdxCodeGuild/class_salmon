



import requests



snowman_pics = ['''



 (   ) 
''', '''


 (   )
 (   ) 
''', '''

 (   )
 (   )
 (   ) 
''', '''

 (   )
 (   )
 ( : )
''', '''

 (   )
 ( : )
 ( : )
''', '''

 ( . )
 ( : )
 ( : )
''', '''
 _===_ 
 ( . )
 ( : )
 ( : )
''', '''
 _===_ 
 ( .O)
 ( : )
 ( : )
''','''
 _===_ 
 (-.O)
 ( : )
 ( : )
''', '''
 _===_ 
 (-.O) 
<( : )
 ( : ) 
''', '''
 _===_ 
 (-.O) 
<( : )\\
 ( : ) 
''']


# print(snowman_pics[0])
# print(len(snowman_pics))
# print(snowman_pics[-1])




def get_random_word():
    url = 'https://random-word-api.herokuapp.com/word/?swear=0' # url of the web API
    response = requests.get(url) # send a GET request to the url
    data = response.json() # take the JSON in response and turn it into a list
    word = data[0] # get the first element of the list
    return word # return it



#          i =   0    1    2    3    4 
# word       = ['a', 'p', 'p', 'l', 'e']
# blank_word = ['_', '_', '_', '_', '_']

#   0    1    2    3    4 
# ['a', 'p', 'p', 'l', 'e']
# ['_', 'p', 'p', '_', '_']


# setup ==============================================

# get a random word
word = get_random_word()
# print(word)

# convert the word into list of single-character strings
word = list(word)
# create a list of underscores with the same length
blank_word = []
for char in word:
    blank_word.append('_')


snowman_counter = 0

guessed_letters = []


# game loop ===========================================

# while snowman_counter != len(snowman_pics) and blank_word != word:

while True:
    # show the user the underscore list
    print(' '.join(blank_word))
    print(f'Already guessed: {" ".join(guessed_letters)}')

    # prompt the user for a guess
    guessed_letter = input('Guess a letter or the whole word: ')

    # if guessed_letter in guessed_letters:
    #     print(f'You\'ve aleady guessed \'{guessed_letter}\', please try again')
    #     continue
    
    while guessed_letter in guessed_letters:
        guessed_letter = input('You\'ve already guessed that, please try again: ')
    
    guessed_letters.append(guessed_letter)
    guessed_letters.sort()


    if list(guessed_letter) == word:
        print('Victory!')
        break

    # if the guessed letter is not in the word, increment our snowman counter
    if guessed_letter not in word:
        print(snowman_pics[snowman_counter])
        snowman_counter += 1
        print(f'Guesses remaining {len(snowman_pics) - snowman_counter}')
        # if the user has run out of guesses, break the loop
        if snowman_counter >= len(snowman_pics):
            print(f'Failure! The word was {"".join(word)}')
            break
    else:
        # go through each index in the list of letters
        for i in range(len(word)):
            # if the guessed letter matches the letter at that index
            if guessed_letter == word[i]:
                # change the corresponding underscore to that letter
                # blank_word.append(guessed_letter)
                blank_word[i] = guessed_letter
        
        # if the use has guessed the word, break the loop
        if blank_word == word:
            print('Victory!')
            break

    # display the new guess count / letters guessed






