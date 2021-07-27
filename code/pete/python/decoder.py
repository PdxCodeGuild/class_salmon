decoder_01 = {
    'Z': 'Harry', 
    '#': 'Maude', 
    '!': 'Vinny', 
    'p': 'Sandra' 
}

decoder_02 = {
    '*': ' flew to ',
    '(': ' drove to ',
    '8': ' walked to ',
    'T': ' biked to ',
}

decoder_03 = {
    'n': 'Las Vegas.',
    '^': 'Omaha.',
    '0': 'New Orleans.',
    'Y': 'Portland.'
}

messages = ['!80', 'Z(y']

for message in messages:
    try:
        part01 = decoder_01[message[0]]
        part02 = decoder_02[message[1]]
        part03 = decoder_03[message[2]]

        print(part01 + part02 + part03)

    except KeyError:
        print("Message not properly encoded.")
   