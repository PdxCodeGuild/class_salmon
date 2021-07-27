data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#changed to include peaks at first and last index in to get version 2 to work
def peaks(lst):
    peaks=[]
    for i,num in enumerate(lst):
        if i == len(lst) - 1 and lst[i-1] < num:
            peaks.append(i)
            #print (num)
        elif i == 0 and num > lst[i +1]:
            peaks.append(i)
        elif i == 0 or i == len(lst) - 1:
            #print(num)
            continue
        elif lst[i-1] < num > lst[i+1]:
            peaks.append(i)
    return peaks
def valleys(lst):
    valleys=[]
    for i,num in enumerate(lst):
            if i == 0 or i ==len(lst) - 1:
                continue
            elif lst[i-1] > num < lst[i+1]:
                valleys.append(i)
    return valleys
def peaks_and_valleys(lst):
    peaks_and_valleys= sorted(peaks(lst) +valleys(lst))
    return peaks_and_valleys
def water_caught(lst):
    peak = peaks(lst)
    water=0
    for i,num in enumerate(lst):
        for index in range(len(peak[:-1])):
            if peak[index] < i < peak[index + 1] and num <  min(lst[peak[index]],lst[peak[index+1]]):
                #print (num)
                water+= abs(num - min(lst[peak[index]],lst[peak[index+1]]))
    return water
print(water_caught(data))