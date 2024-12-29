from termcolor import colored
import connectiontoDB as connection_page
import datetime
import Product

def header():             
    # print()
    # print(" "*10,colored(" "*182, color="black", on_color="on_light_blue")) 
    # print(" "*10,colored(" "*75+"\033[1m WELCOME IN SHOPPING APPLICATION"+" "*75, color="blue", on_color="on_light_blue")) 
    # print(" "*10,colored(" "*182, color="black", on_color="on_light_blue")) 
    # print()
    print()
    print()

    print(' '*20,colored(" "*60,color="blue", on_color="on_blue")) 
    print(' '*20,colored(" "*23+"\033[1m  LOGIN PAGE  "+" "*23, color="black", on_color="on_blue")) 
    print(' '*20,colored(" "*60,color="blue", on_color="on_blue")) 
    print()



def login():
    while 1>0:
        id=input("                        Enter Contact Number: ")
        password=input("                        Enter Password: ")

        query="SELECT * FROM `myntra`.`cust` WHERE `password`='"+password+"' and `contactno`='"+id+"';"
        result=connection_page.MYSQL_CONNECTION.getData(query)         #this will return rowcount
        if len(result)==1:
            print()
            # print(result[0][0])
            print(colored("-"*50+"LOGIN SUCCESSFULLY!!!!!!!"+"-"*50,color='blue',on_color="on_green"))
            Product.call(result[0][0])  
            break
        else:
            print(" "*80,colored("Incorrect Password.....Try again....", color="white", on_color="on_red")) 
        
    


def call():
    header()  
    login()  