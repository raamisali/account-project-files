import re


def files_set_up(file_input):
    f = open("accountinfo.txt", "a+")
    f.write(file_input + " ")
    f.close()


def file_add():
    f = open('accountinfo.txt', 'a')
    f.write("\n")
    f.close()


def username_error():
    print("Your username must be at least 4 characters.")
    username_setup()


def username_setup():
    username = input("Create a username: \n • Must have at least 4 characters \n ")
    if len(username) < 4:
        username_error()
    else:
        return files_set_up(username)


def email():
    user_email = input("Enter your email: \n")
    files_set_up(user_email)


def verification_error(verify):
    print("Your passwords do not match.")
    verify_password(verify)


def verify_password(user_password):
    verification_password = input("Verify your password: \n")
    if user_password != verification_password:
        verification_error(user_password)
    else:
        files_set_up(user_password)


def cody():
    import mainf
    mainf.main()


def main():
        username_setup()
        pass_go()
        email()
        file_add()
        cody()


# Password code below

def characters(char):
    if 8 <= len(char) <= 25:
        return char
    else:
        return re_enter_characters()


def re_enter_characters():
    game = input("Length is invalid. Please re-enter password: \n")
    place_holder(game)


def no_spaces(space):
    if ' ' in space:
        return re_enter_no_spaces()


def re_enter_no_spaces():
    game = input("No spaces are allowed. Please re-enter password: \n")
    place_holder(game)


def sign(ex):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(ex) == None:
        return re_enter_sign()


def re_enter_sign():
    game = input("You must have at least one special character. Please re-enter password: \n")
    place_holder(game)


def upper_lower_case(ul):
    if ul.islower():
        return re_enter_case()

    if ul.isupper():
        return re_enter_case()


def re_enter_case():
    game = input("You must have both uppercase and lowercase characters. Please re-enter your password: \n")
    place_holder(game)


def alphanumeric(alpha):
    if not any(i.isdigit() for i in alpha) and any(i.isalpha() for i in alpha):
        return re_enter_alphanumeric()


def re_enter_alphanumeric():
    game = input("Your password must contain numbers & letters. Please re-enter your password: \n")
    place_holder(game)


def place_holder(passwords):
    characters(passwords)
    no_spaces(passwords)
    sign(passwords)
    alphanumeric(passwords)
    upper_lower_case(passwords)
    verify_password(passwords)


def pass_go():
    password = input(
        "Create a password:  \n • 8-25 characters long \n • No spaces \n • Have at least one special character \n • Uppercase & lowercase letters \n • Alphanumeric \n")

    place_holder(password)


# Main method called below


if __name__ == '__main__':
    main()
