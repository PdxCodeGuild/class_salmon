def sum_numbers(numbers):
    # Start with zero total
    total = 0

    # For each index in the numbers list
    for number in numbers:
        total = total + number

    return total


# Create empty list
numbers = []

# Start loop for user inputs
while True:
    # Prompt user
    user_input = input("Enter a number to add to the list or 'q' to quit: ")

    if user_input != "q":
        # Change the input to int
        user_input = int(user_input)

        # Add the numbers to the list
        numbers.append(user_input)

        print(f"Current numbers are {numbers}")


    elif user_input == "q":
        print(f"""
        Numbers: {numbers}

        Sum: {sum_numbers(numbers)}
        """)
        break
