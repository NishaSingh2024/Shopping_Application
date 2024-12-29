from termcolor import colored
import signup
import login
def header():             
    print()
    print(" "*10,colored(" "*182, color="black", on_color="on_light_blue")) 
    print(" "*10,colored(" "*75+"\033[1m WELCOME IN SHOPPING APPLICATION"+" "*75, color="blue", on_color="on_light_blue")) 
    print(" "*10,colored(" "*182, color="black", on_color="on_light_blue")) 
    print()
    print()
    print()

header()   
print(" "*95,"1 - SIGN UP")
print()
print(" "*95,"2 - LOGIN")

print()
print()
choice=input("                  Enter Your Choice : ")

if choice=="1":
    signup.call()
elif choice=="2":
    login.call()
else:
    print(" "*80,colored("Invalid Choice.....", color="white", on_color="on_red"))

