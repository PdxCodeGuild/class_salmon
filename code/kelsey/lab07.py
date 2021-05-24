# Lab 7: ROT Cipher
# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

import string

letters = string.ascii_lowercase
    
code = input('Enter your letters: ')

i = 0

while True:
    i += 1
    if i <= 12:
        cipher = letters[i + 13]
    elif 12 < i < 25: 
        cipher = letters[i - 12]
    break
print(cipher)


code_tuple = tuple(code)

# def rot13(*args):

  
# Index	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m

# cipher_tuple = rot13(entered_letters)
#     print(cipher_tuple)

