username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin":

    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")

else:
    print("Invalid Username")
