import random
import string

print("Welcome to Password Generator!")

#all characters 
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

while True:

    def generate_random_password():
        print("---------------------------")
        length = int(input("Enter password length: "))

        random.shuffle(characters)

        password = []
        for i in range(length):
            password.append(random.choice(characters))

        random.shuffle(password)
        print("---------------------------")
        print("the Generated password: ")
        print("")
        print("".join(password))


    generate_random_password()
    print("---------------------------")
    restart_inp = input("Restart Program? (y/n) :")
    if restart_inp == "yes" or restart_inp == "Yes" or restart_inp == "y" or restart_inp == "YES" :
        continue
    else:
        break
