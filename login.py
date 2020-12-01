username = input("Enter the username: ")
confirm_username = input("Confirm the username: ")
string1 = None
def confirm_username_function():
    global string1
    for i in [1, 2, 3]:
        if confirm_username != username:
            print("both the usernames you entered don't match with each other")
            a = input("Enter the username again: ")
        string1 = a
        if username == string1:
            print("You have successfully confirmed the username")
            break
        if i == 3:
            print("You have atempted three times but you did not succeed")
            exit(0)
confirm_username_function()

password = input("Enter the password: ")
confirm_password = input("Confirm the password: ")
string = None
def confirm_password_function():
    global string
    for i in range(3):
        if confirm_password != password:
            print("both the passwords you entered don't match with each other")
            b = input("Enter the password again: ")
        string = b
        if password == string:
            print("You have successfully confirmed the password")
            break
        if i == 3:
            print("You have atempted three times but you did not succeed")
            exit(0)
confirm_password_function


with open("hashedpasswords.txt", "a") as file:
        file.write("username : {}\n".format(hash(username)))
        file.write("password : {}\n".format(hash(password)))
