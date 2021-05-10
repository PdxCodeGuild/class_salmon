jackalopes = [0,0]

years = 0

while len(jackalopes) < 1000:

    for jackalope in jackalopes:
        if 4 <= jackalope <=8:
            jackalopes.append(0)

    for i in range(len(jackalopes)-1, -1, -1):
        if jackalopes[i] == 10 :
            jackalopes.pop(i)

    for i in range(len(jackalopes)):
        jackalopes[i] += 1
    print(jackalopes)

    years += 1

    print(f"Years passed: {years} Jackalopes: {len(jackalopes)}")


    