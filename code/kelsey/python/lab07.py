# Lab 7: ROT Cipher
# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

import string

letters = string.ascii_lowercase
coded_msg = list(input('Enter your letters: ').lower()) 

def rot13(coded_msg):
    output = []
    for letter in coded_msg:
        i = letters.index(letter)
        if i <= 12:
            output.append(letters[i + 13])
        elif 12 < i < 26:
            output.append(letters[i - 13])
    output = ''.join(output)        
    return output

print(rot13(coded_msg))


# Index	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m



