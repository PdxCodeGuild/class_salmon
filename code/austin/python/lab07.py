def encrypt_rotn(string):
    cipher= 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    #rot = input('To encrypt please enter a whole number from 1-25.  ')
    rot = 13
    for i,letter in enumerate(string):
        if letter in cipher:
            icip = cipher.index(letter)
            if icip + rot > 25:
                encrypted += (cipher[icip + rot - 26])
            else:
                encrypted += (cipher[icip + rot])
        else:
            continue
    return encrypted
