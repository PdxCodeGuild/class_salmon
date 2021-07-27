'''
Group Project 1
Brea
CJ
Jeremy B
Austin
'''


year = 0
population = [0, 0]
total_population = len(population)


def populate():
    global year, population

    while len(population) < 1000:
        print(population)
        year += 1
        pairs = 0
        # population = [(population.remove(i) if i == 10 else i + 1) for i in population]
        population = [i + 1 for i in population]

        for i in population:
            if i >= 10:
                population.remove(i)

        # for i in population:
        #     if i != 10:
        #         i += 1
        #     else:
        #         population.remove(i)

        mating_age = 0
        for jackelope in population:
            if 4 <= jackelope <= 8:
                mating_age += 1
        pairs = mating_age // 2

        while pairs > 0:
            population.append(0)
            population.append(0)
            pairs -= 1

    return year

print(populate())