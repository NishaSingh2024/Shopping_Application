from termcolor import colored
import login
import connectiontoDB as connection_page
import datetime

class Customer:
    def __init__(self,cname,cpassword,ccontactno,caddress,cadded_on):
        self.cname=cname
        self.cpassword=cpassword
        self.ccontactno=ccontactno
        self.caddress=caddress
        self.cadded_on=cadded_on

    def add_cust(self):
        values="'"+self.cname+"','"+self.cpassword+"','"+self.ccontactno+"','"+self.caddress+"','"+str(self.cadded_on)+"'"
        query='''INSERT INTO `myntra`.`cust`(`custname`,`password`,`contactno`,`address`,`added_on`)
                VALUES('''+values+''');'''
        # print(query)
        
        result=connection_page.MYSQL_CONNECTION.ExecuteQuery(query)         #this will return rowcount
        if result>0:
            print()
            print(colored("-"*50+"DETAILS ADDED SUCCESSFULLY!!!!!!!"+"-"*50,color='blue',on_color="on_green"))

            login.call()


           
       






           
def header():             
    # print()
    # print(" "*10,colored(" "*182, color="black", on_color="on_light_blue")) 
    # print(" "*10,colored(" "*75+"\033[1m WELCOME IN SHOPPING APPLICATION"+" "*75, color="blue", on_color="on_light_blue")) 
    # print(" "*10,colored(" "*182, color="black", on_color="on_light_blue")) 
    # print()
    print()
    print()

    print(' '*20,colored(" "*60,color="blue", on_color="on_blue")) 
    print(' '*20,colored(" "*23+"\033[1m  JOIN US     "+" "*23, color="black", on_color="on_blue")) 
    print(' '*20,colored(" "*60,color="blue", on_color="on_blue")) 
    
    # print("\n")

def getdata():
    isvalid=False
    isnamevalid=False
    ispassvalid=False
    iscontactvalid=False
    isaddressvalid=False
    
    while 1>0:
        while 1>0:
            print()
            name=input("                        Enter Your Name: ")
            if name=='':
               print(" "*80,colored("name should not be empty......", color="white", on_color="on_red")) 
            else:
                isnamevalid=True 
                break   

        while 1>0:   
            print()     
            if isnamevalid==True:
                print(" "*80,colored("[hint: password should have 8 characters]",color="blue",on_color="on_light_magenta"))
                password=input("                        Enter Password: ")
                if len(password)!=8:
                    print(" "*80,colored("Invalid Password.....", color="white", on_color="on_red")) 
                else:
                   ispassvalid=True
                   break

        while 1>0:
            print()
            if ispassvalid==True:
                contactnum=input("                        Enter Contact Number: ")
                if len(contactnum)!=10:
                    print(" "*80,colored("Please check your contact number.....", color="white", on_color="on_red")) 
                else:
                    iscontactvalid=True
                    break

        while 1>0:
            print()
            if iscontactvalid==True:
                add=input("                        Enter Address: ")
                if add=='':
                    print(" "*80,colored("invalid address.....", color="white", on_color="on_red")) 
                else:
                    isaddressvalid=True
                    break

        if isnamevalid==True and isaddressvalid==True and ispassvalid==True and iscontactvalid==True:
            added_on=datetime.date.today() 
            c1=Customer(name,password,contactnum,add,added_on)
            c1.add_cust()
            # print("right")                 
            isvalid=True
            break                
                    


# print(colored("Hello, world!", color="white", on_color="on_red")) 
# print(datetime.date.today())
def call():
    header()
    getdata()    



