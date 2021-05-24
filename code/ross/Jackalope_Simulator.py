
#production_age = {1:0, 2:0, 3:0, 4:2, 5:2, 6:2, 7:2, 8:2, 9:0, 10:-2}
populations = [0, 0]

def adds_jackalopes():
    years = 0
    for age in populations:
        if age < 10:
            age += 1
            if age >= 4 and age <= 8:
                populations.append(age)
            elif age == 10:
                populations.remove(10)
    return age, populations, years
print(adds_jackalopes())         

while len(populations) <= 1000:
    print(adds_jackalopes())


'''for i in population:
        if i < 10:
            population += 1
            if i >= 4 and i <= 8:
while population < 10:
        years += 1
        for p in production_age:
            population += production_age[p]'''