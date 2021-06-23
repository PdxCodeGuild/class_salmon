def rot13(phrase, rotation):

    # abc is a string, which is also a list of individual characters put together
    abc = "abcdefghijklmnopqrstuvwxyz"

    # out_phrase is an empty string
    out_phrase = ""

    # For each letter in the phrase
    for char in phrase:

        # 1) In the abc list, find the letters original index
        # 2) Add 13 to the index number
        # 3) To ensure rotation after z, use modulus 26, which will give the remainder (index after rotation)
        # 4) Append each letter to the string 
        out_phrase += abc[(abc.find(char)+rotation)%26]

    return out_phrase

phrase = list(map(str, input().lower().split()))
rotation = 20

print(phrase)

for p in phrase:
    print(rot13(p, rotation))

#print(rot13(phrase, rotation))