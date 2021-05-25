p_and_v = []
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    p = []
    for i in range(len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            p.append(i)
    return p  
print(peaks(data))


def valleys(data):
    v = []
    for i in range(len(data)-1):
        if i == 0:
            pass
        elif data[i] < data[i-1] and data[i] < data[i+1]:
            v.append(i)
    return v 
print(valleys(data))


def peaks_and_valleys(data):
    global peaks, valleys
    p_and_v = []
    for i in peaks(data):
        p_and_v.append(i)    
    for i in valleys(data):
        p_and_v.append(i)
        p_and_v.sort()
    return p_and_v
print(peaks_and_valleys(data))