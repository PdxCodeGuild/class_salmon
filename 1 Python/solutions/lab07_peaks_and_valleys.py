

import random

# i
# 9                                               X                 X
# 8                                            X  X  X           X  X
# 7                       X                 X  X  X  X  X     X  X  X
# 6                    X  X  X           X  X  X  X  X  X  X  X  X  X
# 5                 X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
# 4              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# 3           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# 2        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# 1     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# index 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def draw_peaks_valleys(data):
    rows = max(data)
    cols = len(data)
    for i in range(rows, 0, -1): # iterate over the rows
        for j in range(cols): # iterate over the columns
            if data[j] >= i:
                print('X', end=' ')
            else:
                print(' ', end=' ')
        print() # after drawing the row, go to the next line



# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data = []
# for i in range(20):
#     data.append(random.randint(1, 7))

# level = 5
# direction = 0
# for i in range(20):
#     data.append(level)
#     direction = random.randint(-1, 1)
#     level += direction


draw_peaks_valleys(data)





