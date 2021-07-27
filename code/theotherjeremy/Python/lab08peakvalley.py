data = [1,	2,	3,	4,	5,	6,	7,	6,	5,	4,	5,	6,	7,	8,	9,	8,	7,	6,	7,	8, 9]
data2 = [1,	2,	3,	4,	5,	6,	7,	6,	5,	4,	5,	6,	7,	8,	9,	8,	7,	6,	7,	8,	9]


peak = []
valley = []
all_pv = []


def findit(data):
    for i in range(len(data)):
        if i == 0 or i == ((len(data))-1):
            continue
        elif data[i-1] > data[i] < data[i+1]:
            valley.append(i)
            all_pv.append(i)
        elif data[i-1] < data[i] > data[i+1]:
            peak.append(i)
            all_pv.append(i)
        else:
            pass


findit(data)

# print(
#    f'Peak indices:  {peak} \nValley indices: {valley}\nPeaks and Valleys: {all_pv}')
# ___________________________Testing some other stuff_______________________________


highest = max(data)
counter = 0
while counter < 9:
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    printer1 = []
    for num in data:
        if num < highest:
            printer1.append(' ')
        elif num >= highest:
            printer1.append('x')

    counter += 1
    highest -= 1
    print(' '.join(printer1))


print(' '.join([str(num) for num in data]))
