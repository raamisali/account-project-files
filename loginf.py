import os.path


def login_error():
    print("Your username or password doesn't match our records.")
    main()


def return_back_to_main():
    import mainf
    mainf.main()


def login_information():
    login = input("Enter your username: \n")
    password = input("Enter your password: \n")

    if os.path.isfile('accountinfo.txt'):  # Checking to see if accountinfo text file is created.
        pass  # If not, then called back to mainf module.
    else:
        print("You don't have an account on file.")
        return return_back_to_main()

    chobi = open('accountinfo.txt')
    particular_text = chobi.read().strip().split()
    if login and password not in particular_text:
        return login_error()
    else:
        print("You've logged into your account.")
        chobi.close()
        return return_back_to_main()




def main():
        login_information()


if __name__ == '__main__':
    main()
