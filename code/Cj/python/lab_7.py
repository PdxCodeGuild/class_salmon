# rot_num = 0

def encrypt(msg):
    output = ''
    word = []
    # rot_num = int(input('Enter a Number of rotations between 1 and 13: '))
    ords = [ord(char) for char in msg]
    # print(ords)
    for char in ords:
        if char == ord(' '):
            word.append(char)
        if char >= ord('a') and char <= ord('z'):
            if char <= ord('m'):
                char += 13
                word.append(char)
            else:
                char -= 13
                word.append(char)
        
    # msg = [char - 13  if char >= ord('a') and char <= ord('z') else char + 13 for char in msg] # tried using rot_num instead of 13. can result in non letter characters
    msg = [chr(char) for char in word]
    for char in msg:
        output += char
    return output



UI = (input('Enter message to encrypt: ')).lower()

print(encrypt(UI))


