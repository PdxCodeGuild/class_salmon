# Lab 8: Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks_list = []
    i = 0
    for i, num in enumerate(data):
        i += 1
        if (data[i-1][1]) < (data[i][1]) < (data[i-1][1]):
            peaks_list.append(i)
        
print(peaks(data))

# def valleys(data):

# def peaks_and_valleys(peaks, valleys):


# print(f'Peaks in this dataset: {peaks(data)}\nValleys in this dataset: {valleys(data)}\nPeaks and valleys: {peaks_and_valleys(data)}')

