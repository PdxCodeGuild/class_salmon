data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_list = []
valley_list = []
peaks_and_valleys_list = []

def peaks(data):
    '''finds and returns the index of peaks in a set of data'''
    # start at the second index and go until the second to last index
    for i in range(1, len(data) - 1):    
        if data[i + 1] < data[i] > data[i - 1]:
            peak_list.append(i)
    peaks = (f"Peaks: {peak_list}")
    return peaks
def valleys(data):
    '''finds and returns the index of valleys in a set of data'''
    # start at the second index and go until the second to last index
    for i in range(1, len(data) - 1):
        if data[i + 1] > data[i] < data[i - 1]:
            valley_list.append(i)
    valleys = (f"Valleys: {valley_list}")
    return valleys
def peaks_and_valleys(data):
    '''finds and returns the index of peaks and valleys in a set of data'''
    # start at the second index and go until the second to last index
    for i in range(1, len(data) - 1):
        if data[i + 1] > data[i] < data[i - 1] or data[i + 1] < data[i] > data[i - 1]:
            peaks_and_valleys_list.append(i)
    p_a_v = (f"Peaks and valleys {peaks_and_valleys_list}")
    return p_a_v

print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))