# this function returns the indices of the peaks
def peaks(data):
    peaks_list = []
    for i, num in enumerate(data):
        try:
            if i != 0 and i != -1:
                if data[i] > data[i - 1] and data[i] > data[i +1]:
                    peaks_list.append(i)
        except IndexError:
            pass
    return peaks_list

# this function returns the indices of the valleys
def valleys(data):
    valleys_list = []
    for i, num in enumerate(data):
        try:
            if i != 0 and i != -1:
                if data[i] < data[i - 1] and data[i] < data[i + 1]:
                    valleys_list.append(i)
        except IndexError:
            pass
    return valleys_list

# this function uses the above two functions to compile a single list of the peaks and valleys in order of appearance
def peaks_and_valleys(data):
    peaks_and_valleys = list(valleys(data) + peaks(data))
    return sorted(peaks_and_valleys)

def visual(data):
    line = ''
    for horizontal in range(-9, 0, 1):
        line += ' '
        for i in range(len(data)):
            if data[i] > -horizontal - 1:
                line += "X  "
            elif data[i] <= -horizontal - 1:
                line += "   "
        line += "\n"
    return line

"""    x_list = []
    line = ''
    for i, num in enumerate(data):
        for y in range(num):
            line += '\nX'
        x_list.append(line)
    return x_list"""

# data = list(input("Please input your data: "))
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print("Peaks are located at the following index/indices: ", peaks(data))
print("Valleys are located at the following index/indices: ", valleys(data))
print("Peaks and Valleys are located at the following indices: ", peaks_and_valleys(data))
print("Visually, it looks like this: ")
print(visual(data))
print(data)