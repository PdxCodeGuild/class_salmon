



from rotcipher import RotCipher


rot_cipher = RotCipher(13)

# rot_cipher2 = RotCipher(18)
# print(type(rot_cipher))
# print(type(rot_cipher2))
# print(rot_cipher)
# print(rot_cipher2)

# print(rot_cipher.rot_amount)
# print(type(rot_cipher))
# print(rot_cipher)

text = 'hello'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text) # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text) # hello

