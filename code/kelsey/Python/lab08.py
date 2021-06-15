# Lab 8: Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks = []
    for i in range(len(data)-1): 
        if data[i - 1] < data[i] > data[i + 1]:
            peaks.append(i)
    return peaks

def valleys(data):
    valleys= []
    for i in range(len(data)-1):
        if i == 0:
            continue
        if data[i-1] > data[i] < data[i+1]:
            valleys.append(i)
    return valleys   

def peaks_and_valleys(peaks_and_valleys):
    pav = peaks(data) + valleys(data)
    return sorted(pav)
    

print(f'Peaks: {peaks(data)}\nValleys: {valleys(data)}\nPeaks and valleys: {peaks_and_valleys(data)}')

