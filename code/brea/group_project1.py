'''
Group Project 1
Brea
CJ
Jeremy B
Austin
'''


year_counter = 0
population = [0, 0]
total_population = len(population)

def populate(popualtion):
    while len(population) < 1000:
        population = [(if 1 == 10 population.pop(i) else i += 1) for i in population]
