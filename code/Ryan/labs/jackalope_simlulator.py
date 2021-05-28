jackalope_count = [0, 0]
breeding_min = 4
breeding_max = 8
integer_to_add = 0
loop_counter = 0
total_population = len(jackalope_count)

while len(jackalope_count) <= 1000:
    loop_counter += 1
    for i in range(len(jackalope_count)):
        jackalope_count[i] += 1
    for i in jackalope_count:
        if i >= breeding_min and i <= breeding_max:
            jackalope_count.append(integer_to_add)
    while 11 in jackalope_count: jackalope_count.remove(11)
    print(len(jackalope_count))
    print(f"end of year {loop_counter}\n")