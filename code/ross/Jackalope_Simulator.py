
#production_age = {1:0, 2:0, 3:0, 4:2, 5:2, 6:2, 7:2, 8:2, 9:0, 10:-2}
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



'''for i in population:
        if i < 10:
            population += 1
            if i >= 4 and i <= 8:
while population < 10:
        years += 1
        for p in production_age:
            population += production_age[p]'''