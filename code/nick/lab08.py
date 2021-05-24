#here is the data for Version 1
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#define the function peaks to return the indices of peaks
#lower numbers on bottom left and right (takes three numbers to figure this out)
def peaks(data):
    peak_indices = []
    for i in range(len(data)):
        if i == 0 or i == ((len(data))-1):
            continue
        #won't let me start on the list at 0 or -1 position; added above if statement
        elif data[i-1] < data[i] > data[i+1]:
            peak_indices.append(i)
        elif data[i-1] > data[i] <data[i+1]:
            continue
    return peak_indices
peak_indices = peaks(data) #only got this to work after adding if i == 0 or..., assigned to variable for 3rd function

#define the function 'valleys' - indices of valleys.
#valleys have high numbers on the left and right (basically the opposite of above)

def valleys(data):
    valleys_indices = []
    for i in range(len(data)):
        if i == 0 or i == ((len(data))-1):
            continue
        #won't let me start on the list at -1 position; added above if statement
        elif data[i-1] > data[i] < data[i+1]:
            valleys_indices.append(i) #swapped out valleys_indices.append(data[i]); works now
        elif data[i-1] < data[i] >data[i+1]:
            continue
    return valleys_indices #got rid of print function
valley_indices = valleys(data)#valley should be at 9 and 17 in data; assigned to variable for next function

#define the function 'peaks_and_valleys'. Uses above
#functions to compile single list of peaks and valleys in 
#order of appearance
def peaks_and_valleys(peak_indices, valley_indices):
    zip_peak_valley = zip(peak_indices, valley_indices)
    return zip_peak_valley
#Call the function to test
result = list(peaks_and_valleys(peak_indices, valley_indices))
print(result) #I am not sure why this is appearing as ordered pairs but it is working otherwise.