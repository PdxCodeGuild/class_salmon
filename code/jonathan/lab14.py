import requests
import time
import string

# checks which grammar to use for the initial split
def dore(joke):
    if question(joke) == False:
        comma(joke)
    else:
        list_joke = joke.split("? ")
        return list_joke
    if comma(joke) == False:
        exclamation(joke)
    else:
        list_joke = joke.split(", ")
        return list_joke
    if exclamation == False:
        period(joke)
    else:
        list_joke = joke.split("! ")
        return list_joke
    if period(joke) == True:
        list_joke = joke.split(". ")
        return list_joke
    else:
        list_joke = joke.split(". ")
        return list_joke
# grammar splits
def question(joke):
    aru = joke.find("?")
    if aru == -1:
        return False
    else: 
        return True
def comma(joke):
    aru = joke.find(",")
    if aru == -1:
        return False
    else: 
        return True
def exclamation(joke):
    aru = joke.find("!")
    if aru == -1:
        return False
    else: 
        return True
def period(joke):
    aru = joke.find(".")
    if aru == -1:
        return False
    else: 
        return True
# takes the list and splits them into two strings
def hataraku(list_joke):
    punchline = list_joke.pop()
    delivery = "".join(list_joke)
    print(delivery)
    return punchline
# takes two strings and adds timing
def omiyagi(punchline):
    time.sleep(6)
    print(punchline)

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
data = response.json()

joke = data['joke']

#joke = ""

list_joke = dore(joke)

punchline = hataraku(list_joke)

omiyagi(punchline)

# periods don't work. Saw one joke with a :