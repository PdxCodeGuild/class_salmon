from posixpath import split
import sys, os, io, math

file = "65438-0.txt"
book = open(os.path.join(sys.path[0], "65438-0.txt"))
contents = book.read()
#contents
#print(contents)

# Find words
words = contents.split()
print("number of words: ", len(words))

# Find Chars
total_chars_count = 0
for i in words:
    for i in i:
        total_chars_count += 1

print("total chars: ", total_chars_count)

# Find Sentences
sentences = contents.split(".")
print("total sentences: ", len(sentences))

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def ari_score(chars, words, sentences):
    chars = chars
    words = len(words)
    sentences = len(sentences)

    left_half = (chars/words)*4.71
    print(float(left_half))
    right_half = (words/sentences)*.5
    print(float(right_half))

    ari = math.ceil((left_half + right_half) - 21.43)

    ari_scale.get(ari) 
    grade = ari_scale[ari]["grade_level"]
    age = ari_scale[ari]["ages"]
    output = f"The ARI for {file} is {ari}\nThis corresponds to a {grade} Grade level of difficulty\nthat is suitable for an average person {age} years old."
    return output

print(ari_score(total_chars_count,words,sentences))





