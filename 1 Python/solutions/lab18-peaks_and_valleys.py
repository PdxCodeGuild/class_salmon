###
# peaks_and_valleys.py
# In class solution to lab 18: peaks and valleys
# Takes in as input a list of heights
# Returns the indices of peaks and valleys
###

def peaks(heights):
    """
    returns the indices of peaks
    """
    peaks = []
    # because we are comparing three items at once, 
    # we don't include the first and last indices
    for i in range(1,len(heights)-1):
        left = heights[i-1]
        middle = heights[i]
        right = heights[i+1]
        if left < middle > right:
            peaks.append(i)
    return peaks


def valleys(heights):
    """
    returns the indices of valleys
    """
    valleys = []
    for i in range(1,len(heights)-1):
        left = heights[i-1]
        middle = heights[i]
        right = heights[i+1]
        if left > middle < right:
            valleys.append(i)
    return valleys


def peaks_and_valleys(heights):
    """
    returns the indices of peaks and valleys in order appearance in the original data
    """
    p = peaks(heights)
    v = valleys(heights)
    return sorted(p + v)


def draw(heights):
    """
    returns string representation of mountain
    """
    mountain = []
    peak = max(heights)
    while peak > 0:
        row = ['X' if height >= peak else ' ' for height in heights]
        mountain.append(''.join(row))
        peak -= 1
    return '\n'.join(mountain)


def draw_water(heights):
    """
    returns string representation of mountain with water filled in
    """
    p = [0] + peaks(heights) + [len(heights)-1] # add the first and last indices
    mountain = []                               # initialize mountain with no rows
    current_height = max(heights)               # initialize current height as highest height
    water_height = 0                            # initialize water height to 0
    current_peak_idx = 0                        # initialize current peak to 0

    while current_height > 0:                             # loop over every row of our mountain
        row = []
        for i in range(len(heights)):           # loop over every index in heights
            if i in p:                          # if i is the location of a peak,
                current_peak_idx = i            # set current peak to i
                if i < len(heights)-1:          # find next peak 
                    peak_idx = p.index(i)
                    next_peak_idx = p[peak_idx + 1]
                    # set the water height to the shorter peak height
                    if heights[i] < heights[next_peak_idx]:
                        water_height = heights[i]
                    else:
                        water_height = heights[next_peak_idx]

            height = heights[i]
            if height >= current_height:        # if this height >= current_height 
                row.append('X')                 # draw mountain
            else: # calculate whether to draw water
                # if the current index is between two peaks, draw water to the lower peak height
                if current_peak_idx < i <= next_peak_idx:
                    if height < water_height >= current_height:
                        # print(f'i={i}, current_peak={current_peak_idx}, next_peak={next_peak_idx}, this_height={height}, water_height={water_height}')
                        row.append('o')
                    else: 
                        row.append(' ')
                else: # draw blank
                    row.append(' ')


        mountain.append(''.join(row))
        current_height -= 1
    return '\n'.join(mountain)    


def draw_to_file(heights, filename):
    mountain = draw(heights)
    mountain_with_water = draw_water(heights)
    with open(filename, 'w') as f:
        print(heights, file=f)
        f.write(mountain)
        f.write('\n')
        f.write(mountain_with_water)



if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(data)
    print(draw(data))
    print('peaks', peaks(data))              # → [6, 14]
    print('valleys', valleys(data))            # → [9, 17]
    print('peaks_and_valleys', peaks_and_valleys(data))  # → [6, 9, 14, 17]
    print()
    print(draw_water(data))
    draw_to_file(data, 'mountains.txt')

    data = [1, 1, 1, 1, 1]
    print(data)
    print(draw(data))
    print('peaks', peaks(data))              # → [] empty list
    print('valleys', valleys(data))            # → []
    print('peaks_and_valleys', peaks_and_valleys(data))  # → []
    print()
    print(draw_water(data))

    data = [3, 2, 1, 2, 3]
    print(data)
    print(draw(data))
    print('peaks', peaks(data))              # → [] empty list
    print('valleys', valleys(data))            # → [2]
    print('peaks_and_valleys', peaks_and_valleys(data))  # → [2] 
    print()
    print(draw_water(data))

    data = [1, 2, 3, 2, 1]
    print(data)
    print(draw(data))
    print('peaks', peaks(data))              # → [2] 
    print('valleys', valleys(data))            # → []
    print('peaks_and_valleys', peaks_and_valleys(data))  # → [2] 
    print()
    print(draw_water(data))
