password = str(input("Create your password: "))
password2 = str(input("Enter your password: "))
while not password2 == password:
    print("Incorrect! Try Again")
    password2 = str(input("Enter your password: "))
else:
    print("access granted")