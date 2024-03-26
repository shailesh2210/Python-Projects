password = input("Enter your Password? ")

def view_pass():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            pass

def add_pass():
    name = input("Account Name: ")
    pwd = input("Password : ")

    with open("passwords.txt", "a") as f:
        f.write(name + "| " + pwd + "\n")       

while True:
    mode = input("Would youe like to add a new password or view password or q for break : ")
    if mode == "q":
        break

    if mode == "view":
        view_pass()
    elif mode == "add":
        add_pass()
    else:
        print("Invalid")

view_pass()
add_pass()
        
