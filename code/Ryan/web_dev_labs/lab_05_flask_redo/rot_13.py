def rot13(phrase, rotation):

    # abc is a string, which is also a list of individual characters put together
    abc = "abcdefghijklmnopqrstuvwxyz"

    # out_phrase is an empty string
    out_phrase = ""

    # How many times to rotate
    rotation = int(rotation)
    #print(rotation)

    # Separate the words by spaces and make lower case
    phrase = list(map(str, phrase.lower().split()))
    #print(phrase)

    # Combine the words back into a list
    for word in phrase:

        # For each letter in the word
        for char in word:
            # 1) In the abc list, find the letters original index
            # 2) Add 13 to the index number
            # 3) To ensure rotation after z, use modulus 26, which will give the remainder (index after rotation)
            # 4) Append each letter to the word 
            out_phrase += abc[(abc.find(char)+rotation)%26]

        out_phrase += " "


    return out_phrase   



#print(rot13("this is a test", 10))
