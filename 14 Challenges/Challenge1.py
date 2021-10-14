# ============================== AUTHENTICATION PROGRAM WRITTEN IN PYTHON ==============================================
pin = '0808'
counter = 3
user_input = input("Please enter PIN: ")

while user_input == pin:
    print("Access Granted")
else:
    if user_input != pin:
        counter -= 1
        print(f"invalid password!\t{counter} trials remaining.\n\n")
        second_user_input = input("Please re-enter password: ")
        # SECOND TRY
        if second_user_input == pin:
            print("Access Granted")
        elif second_user_input != pin:
            counter -= 1
            print(f"invalid password!\t{counter} trials remaining.\n\n")
            third_user_input = input("Please re-enter password: ")
            # THIRD TRY
            if third_user_input == pin:
                print("Access Granted")
            elif third_user_input != pin:
                counter -= 1
                print(f"invalid password!\t{counter} trial remaining.\n\n")
            if counter == 0:
                print("Authentication failed!\tPlease try again later.")
