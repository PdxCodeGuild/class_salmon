import random

eyes_list = [':',';','=','$']

nose_list = ['*','v','^',' ','-','^{','^}']

mouth_list = ['{','}','(',')','o','3','c','|','/','\\']


emoticon_count = int(input('How many emotes do you want to generate? '))

count = 0

while count < emoticon_count:
    eyes = random.choice(eyes_list)
    nose = random.choice(nose_list)
    mouth = random.choice(mouth_list)

    print(f'{eyes}{nose}{mouth}\n')
    count+=1
