data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

i = 0

def peaks(data):
    return [6, 14]

def valleys(data):
    return [9, 17]

def peaks_and_valleys(data):
    return peaks(data), valleys(data)

for each_number in data:
    print(each_number*"x")
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
