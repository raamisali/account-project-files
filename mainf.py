import createnewaccount
import loginf
import restoreaccount


def get_option():
    options = {
        "LOGIN": 1,
        "CREATE NEW ACCOUNT": 2,
        "RESTORE ACCOUNT": 3,
    }

    print("------------------------")
    for options, choices in options.items():
        print(options + ' - ' + str(choices))
    print("------------------------")

    while True:
        try:
            user_option = (input("Select an option 1-3: \n"))
            user_option = int(user_option)
            if user_option < 1 or user_option > 3:
                raise Exception
        except ValueError:
            print("Invalid response.")
        except Exception:
            print("Invalid option.")
        else:
            return user_option

def main():
    user_ = get_option()

    if user_ == 1:
        loginf.login_information()
    if user_ == 2:
        createnewaccount.main()
    if user_ == 3:
        restoreaccount.main()

if __name__ == '__main__':
    while True:
        main()