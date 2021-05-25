import warnings

warnings.filterwarnings('ignore')

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#print(data)

peaks_list = []
valleys_list = []

def peaks(data):
    for i in range(0, len(data)):
        print(i, data[i])

        if (data[i] - data[i - 1]) == (data[i + 1] - data[i]):
            print("up")
    return 

def valleys(data):
    for i in range(0, len(data)):
        print(i, data[i])

        if (data[i] - data[i - 1]) == (data[i + 1] - data[i]):
            print("down")
    return

def peaks_and_valleys(peaks, valleys):
    return



print(peaks_list)
peaks(data)

print(valleys_list)
valleys(data)
