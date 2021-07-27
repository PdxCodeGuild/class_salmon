import requests
import time

# checks which grammar to use for the initial split
def dore(joke):
    if question(joke) == True:
        list_joke = joke.split("? ")
        return list_joke
    else:
        comma(joke)
    if comma(joke) == True:
        list_joke = joke.split(", ")
        return list_joke
    else:
        exclamation(joke)
    if exclamation == True:
        list_joke = joke.split("! ")
        return list_joke
    else:
        period(joke)
    if period(joke) == True:
        list_joke = joke.split(". ")
        return list_joke
    else:
        colon(joke)
    if colon(joke) == True:
        list_joke = joke.split(": ")
        return list_joke
    else:
        question(joke)  
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
def colon(joke):
    aru = joke.find(":")
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
def jodan(punchline):
    time.sleep(6)
    print(punchline)

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
data = response.json()

joke = data['joke']

list_joke = dore(joke)

punchline = hataraku(list_joke)

jodan(punchline)