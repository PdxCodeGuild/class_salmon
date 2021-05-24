jackalope_count = [0, 0]

counter = 1
# while jackalope population is less than (1000 = target)
while len(jackalope_count) < 10:
    for i in range(len(jackalope_count)):
        jackalope_count[i] += 1
    if i in jackalope_count >= 4 and jackalope_count <= 8:
        jackalope_count.append(counter)


print(jackalope_count)


"""
jackalope_count.append

jackalope_baby = []

jackalope_old = []


# total_pop = (jackalope_baby + jackalope_pop) - jackalope_old

while jackalope_age < 11:
    jackalope_age += 1

    if 8 >= jackalope_age >= 4:
        jackalope_baby += 2


jackalope_pop_at_each_age = [range(0, 10)]
print(jackalope_pop_at_each_age)

#generation  = [2, 2, 2, 4, 6, 8, 10]
jack_dict = {'0': 2, '1': 0, '2': 0, '3': 0, '4': 0,
             '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}
jackos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in jackos:
    breeders = jackos[4:9]

breeders // 2 = x
jackos[0] += x


x = generation[4:7]
for x in x:
    x += 1
    print(x)

print(x)
print(generation[4:7])
"""
