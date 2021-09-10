# Create a dictionary of profiles
profile_1 = {
    "username": "test_user1",
    "password": "Password1"
}
profile_2 = {
    "username": "test_user2",
    "password": "Password2"
}
profile_3 = {
    "username": "test_user3",
    "password": "Password3"
}

profiles = [profile_1, profile_2, profile_3]


# print(profiles[0:])


# Function for logging in
def login(username_attempt, password_attempt, profile):
    if username_attempt == profile.get("username") and password_attempt == profile.get("password"):
        return True

    else:
        return False


remaining_attempts = 2

# Login Loop
while True:

    username_attempt = input("Enter your username: ")
    password_attempt = input("Enter your password: ")

    profile_counter = 2

    for profile in profiles:
        """
        print(f"Using creds: {username_attempt}, {password_attempt}")
        print(f"Testing against profile {profile}")
        print(f"Login Result: {login(username_attempt, password_attempt, profile)}")
        """

        login_result = (login(username_attempt, password_attempt, profile))

        """
        print(f"Profile counter: {profile_counter}")
        print(f"Remaining Attempts: {remaining_attempts}")
        """

        # if the login result is true, login the user
        if login_result:
            print(f"Login Successful. Welcome {username_attempt}")
            exit()
            break

        # If login is false, and profiles remain to be checked
        if not login_result and profile_counter != 0:
            # Iterate through to the next profile
            profile_counter -= 1
            continue

        # if the login result is false, all profiles have been checked, and attempts remain
        elif not login_result and profile_counter == 0 and remaining_attempts != 0:
            # Inform the user
            print(f"\nIncorrect login. {remaining_attempts} login attempt(s) remaining\n")
            # Subtract 1 from the remaining attempts
            remaining_attempts -= 1
            # Try login again
            continue

        # If login result is false, all profiles have been checked, and no attempts remain
        elif not login_result and profile_counter == 0 and remaining_attempts == 0:
            print("Your login has been unsuccessful three times! Try again later. Goodbye!")
            exit()
            break

        """
        elif login_result == False and login_count < 3:
            login_count += 1
            login_count_left = 4 - int(login_count)
            print(f"\nIncorrect login. {login_count_left} login attempt(s) remaining\n")

            retry = input("Would you like to try and login again? (y/n): ")
            retry.lower()

            if retry == "y" or retry == "yes":
                break_out_flag = True
                break

            else:
                exit()
                break



        if login_result:
            print(f"Login Successful. Welcome {username_attempt}")
            exit()
            break

        elif not login_result and login_count < 3:
            break_out_flag = True

            try_again = input(f"Login Failed. Username or Password incorrect.\nEnter 'y' to continue or 'n' to quit: ")

            if try_again != "y":
                print("Please restart the program.")
                exit()

            else:
                # Increment the counter
                login_count += 1
                login_count_left = 4 - int(login_count)
                print(f"\nThere is {login_count_left} login attempt(s) left.\n")
                break

        else:
            print("Your login has been unsuccessful three times! Try again later. Goodbye!")
            exit()
"""
