from termcolor import colored
import connectiontoDB as connection_page
import datetime
import pandas as pd
import random

def header():             
    # print()
    # print(" "*10,colored(" "*182, color="black", on_color="on_light_blue")) 
    # print(" "*10,colored(" "*75+"\033[1m WELCOME IN SHOPPING APPLICATION"+" "*75, color="blue", on_color="on_light_blue")) 
    # print(" "*10,colored(" "*182, color="black", on_color="on_light_blue")) 
    # print()
    # print()
    # print()
    print("*"*125)
    print(' '*20,colored(" "*60,color="blue", on_color="on_blue")) 
    print(' '*20,colored(" "*21+"\033[1m  CLOTHING OPTION "+" "*21, color="black", on_color="on_blue")) 
    print(' '*20,colored(" "*60,color="blue", on_color="on_blue")) 
    print()
    print()
    
    


def display():
    genderchoice=''
    print(" "*20,"SEARCH BY GENDER")
    print()
    print(" "*20,"1 - MALE       2-FEMALE       3-KIDS")
    print()
    gender=input("                    ENTER YOUR CHOICE:  ")
    if gender in "123":
        if gender=='1':
            genderchoice='M'
        elif gender=='2':
            genderchoice='F'
        elif gender=='3':
            genderchoice='K'
        else:
            print(" "*80,colored("Invalid Choice.....", color="white", on_color="on_red")) 
            
    if genderchoice!='':
        global getGender
        getGender=genderchoice

        query="SELECT PRODID,BRAND,PNAME,GENDER,SIZE,PRICE,QUANTITY FROM `MYNTRA`.`product` WHERE GENDER='"+genderchoice+"' AND QUANTITY>0;"
        result=connection_page.MYSQL_CONNECTION.getData(query)         #this will return rowcount
        if len(result)>=1:
            for i in result:
                print()
                print(" "*20+f"| BRAND : {i[1]}   ")
                print(" "*19,colored(f"| {i[2]}              ",color="black", on_color="on_light_blue"),end='')
                print(" "*19,colored(f" CODE :  {i[0]} ",color="light_red", on_color="on_grey"))

                print(" "*20+f"| GENDER : {i[3]}              SIZE : {i[4]}              QUANTITY LEFT IN STOCK: {i[6]}")
                print(" "*20+f"| PRICE : Rs. {i[5]}/-             ")
                print()
                print(" "*20+"-"*100)



def AddToCart(id):
    cart_list={}
    while 1>0:
        print()
        print()
        print(" "*20,"FOLLOWING ACTIONS YOU CAN PERFORM:")
        print("\n"," "*20,"1 - Add Items To the Cart\n"," "*20,"2 - Display Items already Added To the CART\n"," "*20,"3 - Remove Item from the CART\n"," "*20,"4 - Empty the CART\n"," "*20,"5 - Place Order\n"," "*20,"6 - Exit")
        print()
        choice=input("                    Enter Your Choice: ")
        if choice in '123456':
            if choice=='1':
                print()
                code=input("                    Enter Code of Product which You want to ADD TO YOUR CART(AT A TIME 1 ONLY): ")
                quantity=input("                    Enter Quantity: ")
                print()
                if checkPid(code) and len(getAmountAndQuantity(code))>0:
                    
                    amt=getAmountAndQuantity(code)[0]
                    original_qty=getAmountAndQuantity(code)[1]

                    ordered_on=datetime.date.today() 
                

                    if original_qty>=int(quantity):
                        value=[id,code,quantity,amt,ordered_on,original_qty]
                        cart_list[code]=value
                        print(" "*20,colored("-"*30+"Added to CART!!!!!!!"+"-"*50,color='black',on_color="on_light_grey"))
                        
                    else:
                        print(" "*80,colored("QUANTITY IS OUT OF RANGE....", color="white", on_color="on_red"))     
                else:
                    print(" "*80,colored("Invalid CODE.....Please Enter Correct CODE....", color="white", on_color="on_red"))  
                



            elif choice=='2':
                print()
                print(" "*20+"-"*100)
                if len(cart_list)>0:
                    for k in cart_list:
                        query="SELECT PRODID,BRAND,PNAME,GENDER,SIZE,PRICE,QUANTITY FROM `MYNTRA`.`product` WHERE PRODID="+cart_list[k][1]+";"
                        result=connection_page.MYSQL_CONNECTION.getData(query)         #this will return rowcount
                        if len(result)>=1:
                            for i in result:
                                print()
                                # print(" "*20+f"| BRAND : {i[1]}   ")
                                print(" "*19,colored(f"| {i[2]}              ",color="black", on_color="on_light_blue"),end='')
                                print(" "*19,colored(f" CODE :  {i[0]} ",color="light_red", on_color="on_grey"))

                                print(" "*20+f"| GENDER : {i[3]}              SIZE : {i[4]}              QUANTITY LEFT IN STOCK: {i[6]}")
                                print(" "*20+f"| PRICE : Rs. {i[5]}/-             ")
                                print()
                                print(" "*20+"-"*100)
                else:
                    print(" "*20,colored(f"THERE IS NO ITEMS IN YOUR CART....              ",color="blue", on_color="on_light_green"),end='')



                          
            elif choice=='3':
                code_for_remove=input("                    Enter CODE of Product which you want to remove from your CART: ")
                if code_for_remove in cart_list:
                    cart_list.pop(code_for_remove)
                    print(colored("-"*50+"Item Removed from your CART....."+"-"*50,color='blue',on_color="on_green"))
                else:
                    print(" "*80,colored("NO SUCH ITEM IS THERE IN YOUR CART.....PLEASE CHECK YOUR CODE....", color="white", on_color="on_red")) 



            elif choice=='4':
                cart_list.clear()
                print(colored(" "*20,"-"*50+"CART CLEARED...."+"-"*50,color='blue',on_color="on_green"))

            elif choice=='5':
                
                new_lst=list(getName(id))
                for i in new_lst:
                    name=i[0]
                    address=i[2]
                    contactnum=i[1]
                


                print()
                print()
                bum=random.randint(11111,99999)
                print(" "*30,"BILL NO : "+str(bum)+" "*110)
                print(" "*30,"."*130)
                print(" "*30,"NAME : "+name+"                            "+" "*50+"PHONE NO.: "+contactnum+" "*10)
                print(" "*30,"."*130)

                print()
                if len(cart_list)>0:
                    sum=0
                    for k in cart_list:
                        price=int(cart_list[k][2])*int(cart_list[k][3])
                        query="SELECT PRODID,BRAND,PNAME,GENDER,SIZE,PRICE,QUANTITY FROM `MYNTRA`.`product` WHERE PRODID="+cart_list[k][1]+";"
                        result=connection_page.MYSQL_CONNECTION.getData(query)         #this will return rowcount
                        if len(result)>=1:
                            print()
                            for i in result:
                                
                                print(" "*30,f" | {i[2]}      {i[3]}      {i[4]}       {i[5]}      {cart_list[k][2]}                   Rs. "+str(price)+"   ")
                                
                                sum+=price
                    print()            
                    print(" "*30,"."*130)
                    print(" "*30,"  Total Amount : "+str(sum)+" "*120)           
                    print(" "*30,"."*130)


                    print()
                    print()
                    print(" "*20,"CHOOSE PAYMENT MODE:    1 - CASH ON DELIVERY                 2 - CARD")
                    c=input("                     Enter Your Choice: ")
                    status=False
                    if c in "12":
                        if c=='1':
                            entered_amt=input("                     Enter Amount For Payment : ")
                            if int(entered_amt)==sum:
                                status=True
                            else:
                               
                                print(" "*80,colored("Incorrect Amount........", color="white", on_color="on_red")) 
                                status=False

                        elif c=='2':
                            pin=input("                     Enter PIN CODE : ")  
                            entered_amt=input("                     Enter Amount For Payment : ")
                            if int(entered_amt)==sum:
                                status=True
                            else:
                                print(" "*80,colored(" "*50+"Incorrect Amount........", color="white", on_color="on_red"))

                                status=False      
                


                    if status==True:
                        allinserted=False
                        for k in cart_list:
                            if place_order(cart_list[k][0],cart_list[k][1],cart_list[k][2],cart_list[k][3],cart_list[k][4],cart_list[k][5]):
                                print()
                                allinserted=True
                                
                            else:
                                print()
                                allinserted=False
                                
                        if allinserted==True:
                            print()
                            print(" "*20,colored("-"*50+"ORDER PLACED SUCCESSFULLY!!!!!"+"-"*50,color='blue',on_color="on_green"))
                            cart_list.clear()
                        else:
                            print(" "*80,colored(" "*50+"PLEASE CHECK THERE IS SOME ISSUE.....", color="white", on_color="on_red"))



            elif choice=='6':
                break
        else:
            print(" "*80,colored("Invalid Option.....", color="white", on_color="on_red")) 


def update_quantity(id,code,quantity,amt,ordered_on,original_qty):
    rem=int(original_qty)-int(quantity)
    query="UPDATE `MYNTRA`.`PRODUCT` SET QUANTITY="+str(rem)+" WHERE PRODID="+code+";"
       
    result=connection_page.MYSQL_CONNECTION.ExecuteQuery(query)         #this will return rowcount
    if result>0:
        return True
    else:
        return False 
    
# have to check
def place_order(id,code,quantity,amt,ordered_on,original_qty):
    price=int(amt)*int(quantity)
    query="INSERT INTO `myntra`.`cust_prod`(`custid`,`prodid`,`quantity`,`Amount`,`ordered_on`) VALUES("+str(id)+","+code+","+quantity+","+str(price)+",'"+str(ordered_on)+"');"
    # print(query)   
    result=connection_page.MYSQL_CONNECTION.ExecuteQuery(query)         #this will return rowcount
    if result>0:
        if update_quantity(id,code,quantity,amt,ordered_on,original_qty):
            return True
        else:
            return False
    else:
        return False   
     
def checkPid(pid):
    query="SELECT PRODID  FROM `MYNTRA`.`product` WHERE PRODID="+pid+";"
    result=connection_page.MYSQL_CONNECTION.getData(query)         #this will return rowcount
    if len(result)>=1:
        return True
    else:
        return False
    
def getName(cid):
    query="SELECT custname,contactno,address FROM `myntra`.`cust` where custid="+str(cid)+";"
    result=connection_page.MYSQL_CONNECTION.getData(query)         #this will return rowcount
    if len(result)>=1:
        return result
    else:
        return []  

def getAmountAndQuantity(pid):
    l=[]
    global getGender

    query="SELECT PRICE,QUANTITY  FROM `MYNTRA`.`product` WHERE PRODID="+pid+" and GENDER='"+getGender+"';"
    result=connection_page.MYSQL_CONNECTION.getData(query)         #this will return rowcount
    if len(result)>=1:
        l.append(result[0][0])
        l.append(result[0][1])
    return l    



def call(id):
    
    header()  
    display() 
    AddToCart(id) 

# call(id)    