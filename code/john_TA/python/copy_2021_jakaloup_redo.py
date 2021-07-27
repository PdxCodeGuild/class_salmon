# NOTE do v2!

def main():
    population = [0, 0, 10, 10 ]  # target 1000
    year_current = 0
    year_end = 5

    while len(population) < 1100:  # many diff ways you could do this, by year for example
        reproductive_population = 0
        year_current += 1
        print(f'~~~~~~~~~~~~~year = {year_current}, start pop: {population}, len(population)= {len(population)}')        
        
        # count the reproductive potential... 
        for individual in population:
            if 4 <= individual <= 8:
                reproductive_population += 1

        # ... and add that # babies...
        for x in range(reproductive_population):
            population.append(0)

        print(f'killing elderly!')
        while 10 in population:
            population.remove(10)

        print(f'~~~~~~~~~~~~~year = {year_current}, END pop: {population}, len(population)= {len(population)}')      
        for i in range(len(population)): # add one to each age.
            population[i] += 1
    
    print(f'year = {year_current}, len(population)= {len(population)}')
    return population

main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # https://github.com/PdxCodeGuild/class_salmon/blob/main/1%20Python/labs/jackalope.md

# Mob Programming: Jackalope Simulator
# Version 1

# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

#     Jackalopes are reproductive from ages 4-8 and die at age 10.
#     Gestation is instantaneous. Each gestation produces two offspring.
#     Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

# With these conditions in mind, we can represent our population as a list of ints.
# Version 2

# Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We 
# can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. 
# A jackalope will have the following properties:

#     name
#     age
#     sex
#     whether they're pregnant

# Jackalopes can only mate with those immediately around them. Every generation Jackalopes are 
# randomly shuffled.