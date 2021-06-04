import time
import requests
import re
response = requests.get('https://icanhazdadjoke.com/',
                        headers={'accept': 'application/json'})

# look for 200 series response
# print(response)

# format into dictionary
data = response.json()
# print(data)

joke = data["joke"]
print(joke)
#joke = 'Why did the m&m go to school. Because it wanted to be a Smartie!'
q = joke.find("? ")
p = joke.find(". ")
e = joke.find("! ")

split_joke = re.split("\!|\.|\?", joke)


# print(p)
# print(joke[p])

def joker(split_joke):
    if p != -1:
        for i, j in enumerate(split_joke):
            print(j, joke[p])

            time.sleep(2)
    elif q != -1:
        for i, j in enumerate(split_joke):
            print(j, joke[q])

            time.sleep(2)
    elif e != -1:
        for i, j in enumerate(split_joke):
            print(j, joke[e])

            time.sleep(2)
    else:
        print(joke)


question = input('Wanna hear a dad joke? y or n:  ')
if question == 'y':
    time.sleep(1.5)
    print('Okay, here it is:')
    time.sleep(1.5)
    joker(split_joke)

if question == 'n':
    time.sleep(1.5)
    print("Too bad, here it is:")
    time.sleep(1.5)
    joker(split_joke)

'''

'''
