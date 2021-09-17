data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def find_peaks(data):
    peaks = []
    for i in range(len(data)):
        if i == 0 or i == len(data)-1:
            pass
        elif data[i] > data[i+1] and data[i] > data[i-1]:
            peaks.append(i)
    return peaks

def find_valleys(data):
    valleys = []
    for i in range(len(data)):
        if i == 0 or i == len(data)-1:
            pass
        elif data[i] < data [i-1] and data[i] < data[i+1]:
            valleys.append(i)
    return valleys

def pvs(data):
    data_points = []
    for i in range(len(data)):
        if i == 0 or i == len(data)-1:
            pass
        elif data[i] < data[i-1] and data[i] < data[i+1]:
            # valleys.append(i)
            data_points.append(i)
        elif data[i] > data[i+1] and data[i] > data[i-1]:
            # peaks.append(i)
            data_points.append(i)
    return data_points

print(f' The peaks are {find_peaks(data)} and the valleys are {find_valleys(data)}. The list of peaks AND valleys is {pvs(data)} ')