populations = [0, 0]

def adds_jackalopes():
    for i, age in enumerate(populations):
        if age < 10:
           populations[i] += 1
        if 4 <= age <= 8:
            populations.append(0)
    while 10 in populations:
        populations.remove(10)
    return age, populations         

years = 0

while len(populations) <= 1000:
    years += 1
    adds_jackalopes()

print(years)