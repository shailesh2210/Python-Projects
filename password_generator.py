import random
import string

minimum_char = 8

def pass_generator():
    try:
        length = int(input("Enter the length of password you want to generate :"))

        # checks if the pass lenth should minium 8 
        if length >= minimum_char:
            print("Please enter minimum 8 number ")

            print("Generating Password .....")

            
            all_character = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

            password = "".join(random.sample(all_character, length))
            print(password)

            # saving password in the text file for the future use or reference 
            with open("password.txt", "a") as f:
                f.write(password + "\n")
 
        else:
            print("Please Enter minimum 8 ")


    except ValueError:
        print("Please enter a correct value ")

if __name__ == "__main__":
    pass_generator()