"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 08
Version: 1
Date: 5/24/2021

"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peaks = []
    counter = 0
    while counter < len(data):
        if counter == 0:
            counter += 1
        elif counter == (len(data) - 1):
            counter += 1
        else:
            if data[counter] > data[counter - 1] and data[counter] > data[counter + 1]:
                peaks.append(counter)
            counter += 1
    return peaks


def valleys(data):
    counter = 0
    valleys = []
    while counter < len(data):
        if counter == 0:
            counter += 1
        elif counter == (len(data) - 1):
            counter += 1
        else:
            if data[counter] < data[counter - 1] and data[counter] < data[counter + 1]:
                valleys.append(counter)
            counter += 1
    return valleys


def peaks_and_valleys(data):
    counter = 0
    peaks_and_valleys = []
    while counter < len(data):
        if counter == 0:
            counter += 1
        elif counter == (len(data) - 1):
            counter += 1
        else:
            if data[counter] > data[counter - 1] and data[counter] > data[counter + 1]:
                peaks_and_valleys.append(counter)
            elif data[counter] < data[counter - 1] and data[counter] < data[counter + 1]:
                peaks_and_valleys.append(counter)
            counter += 1
    return peaks_and_valleys

print("Peaks and Valleys".center(35, '='))

while True:
    print("Choose one of the following options:")
    print("1) Peaks\n2) Valleys\n3) Peaks and Valleys\n4) Exit")
    choice = input("Choice:")
    try:
        if int(choice) == 1:
            print(f"Peaks: {peaks(data)}")
        elif int(choice) == 2:
            print(f"Valleys: {valleys(data)}")
        elif int(choice) == 3:
            print(f"Peaks and Valleys: {peaks_and_valleys(data)}")
        elif int(choice) == 4:
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid option!")

print("Thank you, please come again!")
