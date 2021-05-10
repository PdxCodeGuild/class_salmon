def cc_valid(original_number):
    list_of_original_number = list(original_number)
    list_of_ints = [int(num) for num in list_of_original_number]
    check_digit = list_of_ints.pop()
    reversed_digits = list(reversed(list_of_ints))
    every_other_doubled = [digit*2 if i % 2 == 0 else digit for i, digit in enumerate(reversed_digits)]
    subtract_nine = [digit-9 if digit > 9 else digit for digit in every_other_doubled]
    digit_sum = sum(subtract_nine)
    second_digit = digit_sum % 10
    return second_digit == check_digit

    # list_of_ints = list(original_number)
    # for i in range(len(list_of_ints)):
    #     list_of_ints[i] = int(list_of_ints[i])

    # check_digit = list_of_ints.pop()

    # list_of_ints.reverse()

    # for i in range(len(list_of_ints)):
    #     if i % 2 == 0:
    #         list_of_ints[i] *= 2

    # for i in range(len(list_of_ints)):
    #     if list_of_ints[i] > 9:
    #         list_of_ints[i] -= 9

    # list_of_ints_sum = sum(list_of_ints)

    # second_digit = list_of_ints_sum % 10

    # second_digit = str(list_of_ints_sum)[1]

    # print(list_of_ints)
    # print(check_digit)
    # print(list_of_ints_sum)
    # print(second_digit)

    # return second_digit == check_digit



print(cc_valid("4556737586899855"))