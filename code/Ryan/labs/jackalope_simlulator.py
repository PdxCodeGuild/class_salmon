jackalope_pop = 2

jackalope_baby = []

jackalope_old = []

jackalope_age = 0

# total_pop = (jackalope_baby + jackalope_pop) - jackalope_old

"""
while jackalope_age < 11:
    jackalope_age += 1

    if 8 >= jackalope_age >= 4:
        jackalope_baby += 2
"""

jackalope_pop_at_each_age = [range(0,10)]
print(jackalope_pop_at_each_age)

generation  = [2, 2, 2, 4, 6, 8, 10] 

x = generation[4:7]
for x in x:
    x += 1
    print(x)

print(x)
print(generation[4:7])