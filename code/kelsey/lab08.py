# Lab 8: Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks_list = []
    i = 0
    for i, num in enumerate(data):
        i += 1
        if data[i-1] < data[i] < data[i-1]:
            peaks_list.append(i)

def valleys(data):
    valleys_list = []
    i = 0
    for i, num in enumerate(data):
        i += 1
        if data[i-1] > data[i] > data[i-1]:
            valleys_list.append(i)

def peaks_and_valleys(peaks, valleys):
    peaks_valleys_list = [peaks(data) + valleys(data)]
    return peaks_valleys_list

print(f'Peaks: {peaks(data)}\nValleys: {valleys(data)}\nPeaks and valleys: {peaks_and_valleys(data)}')

