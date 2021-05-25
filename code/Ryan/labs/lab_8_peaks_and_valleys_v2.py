#data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
"""
i = 0

def peaks(data):

    #enum_data = enumerate(data)
    list([i] for x in enumerate(data))
    
    return 

def valleys(data):
    return [9, 17]

def peaks_and_valleys(data):
    return peaks(data), valleys(data)

#for each_number in data:
#    print(each_number*"x")


x_display = [each_number * "x" for each_number in data]
print(x_display)

print(peaks(data))
#print(valleys(data))
#print(peaks_and_valleys(data))
"""

"""
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Number 1 index
i_num_a = 0

# Number 2 index
i_num_b = 1

# Previous results list
previous_result = []

# Peaks list
peaks = []

# Valleys list
valleys = []

for each_number in data:
    direction = ""

    # Pull number from list 
    # Assign to variable A
    num_a = data[i_num_a]
    print(f"line 11 {num_a}")

    # Pull next in list
    # Assign to variable B
    num_b = data[i_num_b]
    print(f"line 18 {num_b}")

    # Subtract A from B
    latest_result = num_b - num_a
    print(latest_result)
    # If result equals 1, change direction variable to uphill
    if latest_result == 1:
        direction = "uphill"

        # Compare to previous result to see if there's any changes
        if previous_result != latest_result:

            # If the results are not equal, a change from uphill to downhill occured
            # Find the current number index
            new_peak = data[each_number]
            # Add to peak list
            peaks += new_peak # TypeError: 'int' object is not iterable

    # If result equals -1, change direction variable to downhill
    elif latest_result == -1:
        direction = "downhill" 



    i_num_a += 1
    print(i_num_a)
    i_num_b += 1
    print(i_num_b)

    print(direction)
"""
"""
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#i = 0
#for each_number in data:
#    change = data[i+1] - each_number[i]
#    print(change)
#    i += 1
def peaks(data):
    return

def valleys(data):
    return

def peaks_and_valleys(data):
    return

i_0 = data[0]
i_1 = data[1]
i_2 = data[2]
i_3 = data[3]
i_4 = data[4]
i_5 = data[5]
i_6 = data[6]
i_7 = data[7]
i_8 = data[8]
i_9 = data[9]
i_10 = data[10]
i_11 = data[11]
i_12 = data[12]
i_13 = data[13]
i_14 = data[14]
i_15 = data[15]
i_16 = data[16]
i_17 = data[17]
i_18 = data[18]
i_19 = data[19]
i_20 = data[20]
i_21 = data[21]
i_22 = data[22]
i_23 = data[23]
i_24 = data[24]
i_25 = data[25]
i_26 = data[26]
i_27 = data[27]
i_28 = data[28]
i_29 = data[29]
i_30 = data[30]
i_31 = data[31]
i_32 = data[32]
i_33 = data[33]
i_34 = data[34]
i_35 = data[35]
i_36 = data[36]
i_37 = data[37]
i_38 = data[38]
i_39 = data[39]
i_40 = data[40]
i_41 = data[41]
i_42 = data[42]
i_43 = data[43]
i_44 = data[44]
i_45 = data[45]
i_46 = data[46]
i_47 = data[47]
i_48 = data[48]
i_49 = data[49]
i_50 = data[50]




if i_1 - i_0 == 1:
    print("start uphill")

elif i_1 - i_0 == -1:
    print("start downhill")

    if i_2 - i_1 != i_1 - i_0:
        print("direction change")
        if i_2 - i_1 == 1:
            peak += 1 #?
    else:
        print(f"continue {direction}")

        if i_3 - i_2 != i_2 - i_1:
            print("direction change")
            break_flag = False
        else:
            print(f"continue {direction}")

            if i_4 - i_3 != i_3 - i_2:
                print("direction change")
                break_flag = False
            else:
                print(f"continue {direction}")

                if i_5 - i_4 != i_4 - i_3:
                    print("direction change")
                    break_flag = False
                else:
                    print(f"continue {direction}")

                    if i_6 - i_5 != i_5 - i_4:
                        print("direction change")
                        break_flag = False
                    else:
                        print(f"continue {direction}")

                        if i_7 - i_6 != i_6 - i_5:
                            print("direction change")
                            break_flag = False
                        else:
                            print(f"continue {direction}")

                            if i_8 - i_7 != i_7 - i_6:
                                print("direction change")
                                break_flag = False
                            else:
                                print(f"continue {direction}")

                                if i_9 - i_8 != i_8 - i_7:
                                    print("direction change")
                                    break_flag = False
                                else:
                                    print(f"continue {direction}")

                                    if i_10 - i_9 != i_9 - i_8:
                                        print("direction change")
                                        break_flag = False
                                    else:
                                        print(f"continue {direction}")

                                        if i_11 - i_10 != i_10 - i_9:
                                            print("direction change")
                                            break_flag = False
                                        else:
                                            print(f"continue {direction}")

                                            if i_12 - i_11 != i_11 - i_10:
                                                print("direction change")
                                                break_flag = False
                                            else:
                                                print(f"continue {direction}")

                                                if i_13 - i_12 != i_12 - i_11:
                                                    print("direction change")
                                                    break_flag = False
                                                else:
                                                    print(f"continue {direction}")

                                                    if i_14 - i_13 != i_13 - i_12:
                                                        print("direction change")
                                                        break_flag = False
                                                    else:
                                                        print(f"continue {direction}")

                                                        if i_15 - i_14 != i_14 - i_13:
                                                            print("direction change")
                                                            break_flag = False
                                                        else:
                                                            print(f"continue {direction}")

                                                            if i_16 - i_15 != i_15 - i_14:
                                                                print("direction change")
                                                                break_flag = False
                                                            else:
                                                                print(f"continue {direction}")

                                                                if i_17 - i_16 != i_16 - i_15:
                                                                    print("direction change")
                                                                    break_flag = False
                                                                else:
                                                                    print(f"continue {direction}")

                                                                    if i_18 - i_17 != i_17 - i_16:
                                                                        print("direction change")
                                                                        break_flag = False
                                                                    else:
                                                                        print(f"continue {direction}")

                                                                        if i_19 - i_18 != i_18 - i_17:
                                                                            print("direction change")
                                                                            break_flag = False
                                                                        else:
                                                                            print(f"continue {direction}")

                                                                            if i_20 - i_19 != i_19 - i_18:
                                                                                print("direction change")
                                                                                break_flag = False
                                                                            else:
                                                                                print(f"continue {direction}")

                                                                                if i_3 - i_20 != i_20 - i_19:
                                                                                    print("direction change")
                                                                                    break_flag = False
                                                                                else:
                                                                                    print(f"continue {direction}")
"""

"""
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) # apple banana cherry
"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
indexes = [i for i in range(len(data))]
# print(indexes)
# print(data[indexes]) #TypeError: list indices must be integers or slices, not list
data_dict = {
0: data[0],
1: data[1],
2: data[2],
3: data[3],
4: data[4],
5: data[5],
6: data[6],
7: data[7],
8: data[8],
9: data[9],
10: data[10],
11: data[11],
12: data[12],
13: data[13],
14: data[14],
15: data[15],
16: data[16],
17: data[17],
18: data[18],
19: data[19],
20: data[20]
}

print(data)


"""
for each_key in data_dict:
    #print(each_key)
    current_key_value = data_dict.get(each_key)
    next_key_value = data_dict.get(each_key+1)
    #print(next_key_value - current_key_value)
    #result = next_key_value - current_key_value # TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
    #print(type(result)) # <class 'int'>
    #results_list += int(result) #TypeError: 'int' object is not iterable
    #result += results_list #TypeError: unsupported operand type(s) for +=: 'int' and 'list'
    #past_result = result

#past_result = int()
#print(past_result) #TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
"""
"""
num_1 = int()
num_2 = int()

start = True
while start:
    for x in input("Enter a number: "):
        print(x)
        if num_1 == False:
            num_1 = x
            print(f"Adding {x} to num_1")
        elif num_1 == True and num_2 == False:
            num_2 = x 
            print(f"Adding {x} to num_2")
        elif num_1 == True and num_2 == True:
            current_direction = num_2 - num_1
            if current_direction == 1:
                current_direction = "Going up"
            elif current_direction == -1:
                current_direction = "Going down"
            print(f"Subtracting {num_1} from {num_2}. {current_direction} ")
"""

"""
for each_key in data_dict:
    #print(each_key)
    previous_key_value = data_dict.get(each_key-1)
    current_key_value = data_dict.get(each_key)
    next_key_value = data_dict.get(each_key+1)

    if previous_key_value == False:
        continue

    if next_key_value == False:
        continue

    def peak(data):
        if previous_key_value < current_key_value < next_key_value: #TypeError: '<' not supported between instances of 'NoneType' and 'int'
            direction = "uphill"
        return direction 

    print(peak(each_key))


print(data_dict.values())

for x in data_dict:
    print(f"{data_dict.keys()} {data_dict.values()}")
"""

# For each item in the list
# Find the difference
#for x in data:
    #data = data[x+1] #TypeError: 'int' object is not subscriptable

result_list = []


diff_1 = data[1] - data[0]
diff_2 = data[2] - data[1]
diff_3 = data[3] - data[2]
diff_4 = data[4] - data[3]
diff_5 = data[5] - data[4]
diff_6 = data[6] - data[5]
diff_7 = data[7] - data[6]
diff_8 = data[8] - data[7]
diff_9 = data[9] - data[8]
diff_10 = data[10] - data[9]
diff_11 = data[11] - data[10]
diff_12 = data[12] - data[11]
diff_13 = data[13] - data[12]
diff_14 = data[14] - data[13]
diff_15 = data[15] - data[14]
diff_16 = data[16] - data[15]
diff_17 = data[17] - data[16]
diff_18 = data[18] - data[17]
diff_19 = data[19] - data[18]
diff_20 = data[20] - data[19]




result_list.append(diff_1)
result_list.append(diff_2)
result_list.append(diff_3)
result_list.append(diff_4)
result_list.append(diff_5)
result_list.append(diff_6)
result_list.append(diff_7)
result_list.append(diff_8)
result_list.append(diff_9)
result_list.append(diff_10)
result_list.append(diff_11)
result_list.append(diff_12)
result_list.append(diff_13)
result_list.append(diff_14)
result_list.append(diff_15)
result_list.append(diff_16)
result_list.append(diff_17)
result_list.append(diff_18)
result_list.append(diff_19)
result_list.append(diff_20)

print(result_list)

peaks_list = []
valleys_list = []

def peaks(data):
    #print(peaks_list)
    if result_list[data] == -1:
        output = print(f"Peak @ index {data}")
        peaks_list.append(data)
    else:
        output = ""
    return {output}, peaks_list


def valleys(data):
    #print(valleys_list)
    if result_list[data] == 1:
        output = print(f"Valley @ index {data}")
        valleys_list.append(data)
    else:
        output = ""
    return {output}


def peaks_and_valleys(peaks, valleys):
    output = peaks + valleys
    output.sort()
    return output


#start = 0
running_total = 0
i_counter = 0
for each_difference in result_list:
    start = 0
    running_total += each_difference
    #print(f"Start: {start}")
    #print(f"Running total: {running_total}")

    if start < running_total:
        #print(f"Going up @ index {i_counter}")
        running_total = 1 
    elif start > running_total:
        #print(f"Going down @ index {i_counter}")
        running_total = -1
    elif start == running_total:
        #print(f"Direction change @ index {i_counter}")
        peaks(i_counter)
        valleys(i_counter)
        running_total = 0
    i_counter += 1


#print(peaks_list)
#print(valleys_list)
#print(peaks)
print(peaks_and_valleys(peaks_list, valleys_list))