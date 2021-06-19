nums = []
addup = input('Enter a number to add to the list.\nEnter "done" to exit.  ')

while True:
    if addup == 'done':
        break
    else:
        nums.append(addup)
        addup = input(
            'Enter a number to add to the list.\nEnter "done" to exit.  ')

nums2 = []
for num in nums:
    nums2.append(int(num))

final = ((sum(nums2)) / (len(nums2)))
print(f'You entered {nums2} \nThe average of these numbers is {final:.2f}.')
