
import mysql.connector as sql
con = sql.connect(host = "Localhost",user = "root",password = "root" )
cr = con.cursor()
#Check if database exists 
cr.execute("Show databases like 'Railway' ")
result= cr.fetchall()
if(len(result)==0):
    #Database does not exists , the creating it
    cr.execute("Create database ")
    print("database Railway Created")
    cr.execute("Use Railway ")
    print("*********************************************************************")
else:
    #database already exist
    print("Database train already  exists")
    cr.execute("Use train")
    print("**********************************************************************")
    
    
#for train details and information purpose    
cr.execute("Show tables like 'traindetails' ")
result = cr.fetchall()
if (len(result)==0):
    print(" traindetails Table does not exist amd creating it")
    cr.execute("create table traindetails(train_number int auto_increment primary key , tname Varchar(225), tsource varchar(225),tdestination varchar(225)), capacity int(8)")
    
else :
    print(" traindetails Table exists")
#****************************************************************************
    
#For login and passengers details purpose   
cr.execute("show tables like passengers")
result = cr.fetchall()
if(len(result==0)):
    print(" passengers Table does not exist amd creating it")
    cr.execute("create table passenegers(pass_id int auto_increment primary key , name Varchar(225), age int(8) ,contact_no int(8),gender varchar(225), disablity varchar(225))")
else :
    print(" passengers Table exists")
#***************************************************************************88
    
#for booking purpose 
cr.execute("Show tables like trainbook")
result = cr.fetchall()
if(len(result)==0):
    print("Table trainbook does not exists")
    cr.execute("create table trainbook(train_number int(8),pass_id int(8),name varchar(225),source varchar(225),destination(225),seat_no int(8), num_of_tickets int(8))")
else:
    print("Table trainbook exists")
#***********************************************************************************

def showtrains():
    cr.execute("Select * from traintdetails")
    result = cr.fetchall()
    for x in result:
        print(x[0])

####################################################################################
#seates in trains 
T1u = 20 
T1d = 20
T2u = 20
T2d =20

    
    
        
      
        

print("This is a train Booking System ")
print("*************************************************************************")
print()
choice = None

#*********************************************************************************#    
def tbook():
    showtrains()
    print("Please enter the train number for the train booking")
    
    
    name=str(input("Enter your name :-  "))
    age =str(input("Enter your age :-  "))
    loc = str(input("Enter your your location  :- "))
    des = str(input("Enter your Destination :- "))
    gender= str(input("Enter your gender(Male or Female) :- "))
    disablity = input("Are you Disable ?(Enter yes or no:) ")
    if disablity == "yes":
        disablity = True
    elif disablity == "no":
       disablity = False
    else:
     print("Invalid input , please answer in yes or no ")

    
    seat = int(input("Enter number of seats required :- "))
    if(seat == 1) and (gender=="Female" or "female" or "FEMALE"):
        single_lady = True
        print("true")
    else:
        single_lady= False
    
    
        
    
        
    
    

   
    
#***********************************************************************************#
def login():
    name = str(input("Enter your Name : "))
    mobile_no = int(input("enter your mobile number"))
#*************************************************************************************#
def cancel():
    print("Your ride has been cancelled")
#*****************************************************************#
def menu():
    print('''Enter 1 for login 
Enter 2 for train Ticket booking 
Enter 3 for Ticket cancellation ''' )
    global choice
    choice = int(input("Input your choice :-"))
    print(choice)
#*****************************************************************************************#
menu()  
if(choice == 1):
    print()
    login()
elif(choice == 2):
    tbook()
elif(choice == 3):
    print()
    cancel()
else:
    print("Please enter valid choice")
    menu()
#*********************************************************************************#


    
    