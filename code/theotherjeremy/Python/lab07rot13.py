secret = 'This is a test'
secret = input('Tell me your secret:  ')
secret = secret.lower()


english = 'abcdefghijklmnopqrstuvwxyz .'
rot = 'nopqrstuvwxyz .abcdefghijklm'
rot2 = []
for i in rot:
    rot2.append(i)


rot_idx = []
for let in secret:
    if let in english:
        rot_idx.append(english.index(let))


code = []

for indx in rot_idx:
    code.append(rot[indx])


code = ''.join(code)
print(f'Your code is: {code}')
