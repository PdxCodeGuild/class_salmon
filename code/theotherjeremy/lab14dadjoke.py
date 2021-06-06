import time
import requests

response = requests.get('https://icanhazdadjoke.com/',
                        headers={'accept': 'application/json'})

# print(response) <~~~~~ look for 200 series response

data = response.json()  # <~~~~~~~~~ format into dictionary
# print(data) <~~ see the dictionary

joke = data["joke"]

q = joke.find("? ")
p = joke.find(". ")
e = joke.find("! ")


def joker(joke):
    # had to input all the request info inside the function to be able
    # to generate a new joke every time the function was called
    response = requests.get('https://icanhazdadjoke.com/',
                            headers={'accept': 'application/json'})
    data = response.json()
    joke = data["joke"]
    q = joke.find("? ")
    p = joke.find(". ")
    e = joke.find("! ")
    if p != -1:
        print(joke[0:p+1])
        time.sleep(4)
        print(joke[p+2:])
    elif q != -1:
        print(joke[0:q+1])
        time.sleep(4)
        print(joke[q+2:])
    elif e != -1:
        print(joke[0:e+1])
        time.sleep(4)
        print(joke[e+2:])
    else:
        print(joke)


question = input('Wanna hear a dad joke? y or n:  ')

if question == 'y':
    while True:
        time.sleep(1.5)
        print('Okay, here it is:')
        time.sleep(1.5)
        joker(joke)
        again = input('Want another? y or n:  ')
        if again == 'y':
            pass
        else:
            break
if question == 'n':
    time.sleep(1.5)
    print("Too bad, here it is:")
    time.sleep(1.5)
    while True:
        joker(joke)
        again = input('Want another? y or n:  ')
        if again == 'y':
            pass
        else:
            break
