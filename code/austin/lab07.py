def encrypt_rotn(string, rot = int(input('To encrypt please enter a whole number from 1-25.  '))):
    cipher= 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for i,letter in enumerate(string):
        if letter in cipher:
            icip = cipher.index(letter)
            if icip + rot > 25:
                encrypted += (cipher[icip + rot - 26])
                print(letter)
            else:
                encrypted += (cipher[icip + rot])
                print(letter)
                print((cipher[i + rot]))
        else:
            continue
    return encrypted