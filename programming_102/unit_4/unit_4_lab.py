# Strings acquired through user input
word_1 = input("Enter the first word: ").lower()
word_2 = input("Enter the second word: ").lower()

output_1 = word_1
output_2 = word_2
# Sort the letters of each list
word_1 = list(word_1)
word_1.sort()
sorted_word_1 = word_1
# print(sorted_word_1)

word_2 = list(word_2)
word_2.sort()
sorted_word_2 = word_2
# print(sorted_word_2)

new_word_1 = []

new_word_2 = []

# Convert the strings into lists
for w in word_1:
    new_word_1.append(w)

for w in word_2:
    new_word_2.append(w)

# Check if the two list equal
if word_1 != word_2:
    print(f"{output_1} and {output_2} are not anagrams")

elif word_1 == word_2:
    print(f"{output_1} and {output_2} are anagrams")