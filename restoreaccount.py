import os.path
import csv


def cody():
    import mainf
    mainf.main()


def username_or_password():
    email = input("Enter the email linked to your account: \n")
    with open("accountinfo.txt") as f:
        reader = csv.reader(f, delimiter=" ")
        for row in reader:
            if row and row[2] == email:
                print(" ".join(row[:1]))
                break
        else:
            print("This email doesn't exist in our records.")
            main()

def main():
    username_or_password()


if __name__ == '__main__':
        main()
