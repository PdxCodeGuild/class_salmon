# python3 -m install requests
import requests
import random
# import time
# add the suspense for jokes with questions and answers

def jokes():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': "application/json"})
    data = response.json()
    joke = data['joke']
    return print("\n" + joke + "\n")

def search(topic):
    response = requests.get(f'https://icanhazdadjoke.com/search?term={topic}', headers={'Accept': "application/json"})
    data = response.json()
    results = data['results']
    jokes = []
    jokes = [results[i]['joke'] for i, num in enumerate(results)]
    try:
        return print("\n" + random.choice(jokes) + "\n")
    except:
        return print(f"\nSorry we couldn't find {topic} in any of our jokes. Please try again.\n")


r = input("Would you like to get a dad joke?\n'Y' to receive a random joke, 'S' to search for a joke by topic, or hit 'N' to exit: ").upper()

while r == 'Y' or r == 'S':
    if r == 'Y':
        # add joke quantity later
        # quant = int(input("How many random jokes would you like to receive? Pick a number between 1 and 307: "))
        jokes()
        r = input("Would you like to get another dad joke?\n'Y' to receive a random joke, 'S' to search for a joke by topic, or hit any other key to exit: ").upper()
    elif r == 'S':
        search(input("What topic would you like to search for: "))
        r = input("Would you like to get another dad joke?\n'Y' to receive a random joke, 'S' to search for a joke by topic, or hit any other key to exit: ").upper()
    else:
        print("Okay, thanks for reading our jokes!")
        break