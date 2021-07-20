


fizz_counter = 0
buzz_counter = 0
for x in range(100):
    fizz_counter += 1
    buzz_counter += 1
    if fizz_counter == 3 and buzz_counter == 5:
        print('FizzBuzz')
        fizz_counter = 0
        buzz_counter = 0
    elif fizz_counter == 3:
        print('Fizz')
        fizz_counter = 0
    elif buzz_counter == 5:
        print('Buzz')
        buzz_counter = 0
    else:
        print(x + 1)