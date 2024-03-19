import random

print("Hello", input("Tell me your name: "), "Start your Driving Licence Application")

def info():
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    if age < 18:
        print(f"Sorry {name} we can't provide your driving license")
    elif age >18:
        license_list = ["Two license" , "Four License"]
        print("Please enter for which license you're applying for",license_list)
        print("Press 1 for Two Wheeler lLicense ")
        print("Press 2 for Four Wheeler License")
        select_license = int(input("Enter the number that youre applying for : "))
        if select_license == 1:
            print("Sure Enter your details for applying - ", license_list[0])

            birth_certificate = ["Y", "N"]
            a = input("Enter the birth certificate: Y , N ")
            if a == birth_certificate[0]:
                print("OK")
            else:
                print("ok")

            HSC_pass = ["Y", "N"]
            b = input("You have Pass HSC : Y , N ")
            if a == HSC_pass[0]:
                print("OK")
                print("You have to clear HSC for Application for driving license")

            number = int(input("Enter your number :"))
            if len(str(number)) == 10:
                print(f"Thank you {name} we have send an OTP to your Given Number and Register by the given Link")

                otp = str(random.randint(1000, 9999))
                print(otp)

            elif number != 10:
                print(f"Please check the number, Please enter 10 digits {number}")

        else:
            print("Sure Enter your details", license_list[1])
    else:
        print("Sure")

if __name__ == "__main__":
    info()

