
production_age = {1:0, 2:0, 3:0, 4:2, 5:2, 6:2, 7:2, 8:2, 9:0, 10:-2}

def adds_jackalopes():
    population = 2
    years = 0
    while population < 1000:
        for p in production_age:
            population += production_age[p]
        for i in years:
            years += i
    return population, years
    '''for age in populations:
        if age < 10:
            age += 1
            if age >= 4 and age <= 8:
                populations.append(0)
    return age, populations'''
print(adds_jackalopes())         

'''for i in population:
        if i < 10:
            population += 1
            if i >= 4 and i <= 8:'''

'''while population < 10:
        years += 1
        for p in production_age:
            population += production_age[p]'''


