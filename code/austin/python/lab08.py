
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
def peaks(lst):
    peaks=[]
    for i,num in enumerate(lst):
        if i == 0 or i == len(lst) - 1:
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