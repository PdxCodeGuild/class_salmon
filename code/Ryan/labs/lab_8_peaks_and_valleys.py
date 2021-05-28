data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#print(data)

peaks_list = []
valleys_list = []

def peaks(data):
    for i in range(len(data)):
        if i != 0 and i != len(data) - 1:
            if data[i - 1] < data[i] > data[i + 1]:
                #print("peak" , i)
                peaks_list.append(i)
                
        """print(i, data[i])

    for each_number in data:
        print(each_number)"""
    return peaks_list

def valleys(data):
    for i in range(0, len(data)):
        if i != 0 and i != len(data) - 1:
            if data[i - 1] > data[i] < data[i + 1]:
                #print("valley" , i)
                valleys_list.append(i)
            #print(i, data[i])

    return valleys_list

def peaks_and_valleys(data):
    output = peaks(data) + valleys(data)
    output.sort()
    return print(output)

#print(peaks(data))
#print(valleys_list)
#print(valleys(data))
# print(peaks_list)

peaks_and_valleys(data)