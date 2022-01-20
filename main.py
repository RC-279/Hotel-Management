import mysql.connector
import random
import pandas as pd
import time
import datetime
import matplotlib.pyplot as plt

username = input("Enter Your Username : ")
password = input("Enter Your Password : ")
mydb = mysql.connector.connect(user=username, password=password,
                               host='localhost')
mycursor = mydb.cursor()

database_creation = '''create database IF NOT EXISTS hotel_management_rc279'''
mycursor.execute(database_creation)
created_database = mydb.commit()

mydb = mysql.connector.connect(user=username, password=password,
                               host='localhost',
                               database='hotel_management_rc279')
mycursor = mydb.cursor()


# ************************* MYSQL TABLE FUNCTION ************************* #
def auto_table_creation():
    database_creation = '''create database IF NOT EXISTS hotel_management_rc279'''

    customer_registration = '''CREATE TABLE IF NOT EXISTS customer_registration (customer_id varchar (50) Primary key,
        customer_name  varchar (50), customer_age  integer(2), customer_sex  varchar (50),customer_mobile_no  
        varchar (100), customer_email  varchar (150), customer_Nationality  varchar (50),Type_of_document varchar 
        (50), Name_on_document  varchar (50), Customer_no_of_document  integer (50),customer_check_in  Date 
        , check_out Date)'''

    room_booked = '''CREATE TABLE IF NOT EXISTS Room_Booked(Customer_ID integer(100),Room_No integer(10),
       Room_Choice integer(10),room_type varchar (20),No_of_Days integer(10),Room_Rent integer(10))'''

    restaurant_bill = '''create table IF NOT EXISTS restaurant_bill (Customer_ID integer(200), choice_dish varchar(20), 
        quantity integer(20),Particular varchar (50), Total_Bill integer(30))'''

    game_zone = '''create table IF NOT EXISTS game_zone (Customer_ID integer (20), no_of_person int(20), choice_game 
       integer(20), name_of_game varchar(50), Total_Bill integer(25))'''

    shopping_zone = '''create table IF NOT EXISTS shopping_zone (Customer_ID integer (50), choice_particular 
        varchar (50), quantity integer (50), particular_name varchar (50), Total_Bill integer(50))'''

    final_bill = '''create table IF NOT EXISTS final_bill(date_now Date, customer_id integer(100),name_fb_1 
        varchar(100),mobile_mn_1 varchar(100),r_n_1 varchar(100),no_days_1 integer(100),bill_rbo integer(100),
        bill_rb integer(100),bill_gz integer(100), bill_sz integer(100),total_bill integer(100),payment_type 
        varchar(100),status varchar(100))'''

    mycursor.execute(database_creation)
    mycursor.execute(customer_registration)
    mycursor.execute(room_booked)
    mycursor.execute(restaurant_bill)
    mycursor.execute(game_zone)
    mycursor.execute(shopping_zone)
    mycursor.execute(final_bill)
    mydb.commit()
    time.sleep(1)
    print("[+] Tables Has Been Successfully Connected.")


# ************************* MAIN FUNCTIONS ************************* #


def intro():
    print("---------------------------- The Soho Palace ----------------------------")
    print("--------------------------- Welcome To Portal ---------------------------")


def registercust():
    L = []
    customer_id = random.randint(100000, 9999999)
    L.append(customer_id)
    customer_name = input(" \t[1] Enter Customer Name: ")
    L.append(customer_name)
    customer_age = int(input(" \t[2] Enter Age: "))
    L.append(customer_age)
    customer_sex = input(" \t[3] Enter Sex: ")
    L.append(customer_sex)
    customer_moblie_no = input(" \t[4] Enter Mobile no.: ")
    L.append(customer_moblie_no)
    customer_email = input(" \t[5] Enter Email: ")
    L.append(customer_email)
    customer_Nationality = input(" \t[6] Enter Nationality: ")
    L.append(customer_Nationality)
    type_of_document = input(" \t[7] Enter Type Of Document: ")
    L.append(type_of_document)
    name_on_document = input(" \t[8] Enter Name On Document: ")
    L.append(name_on_document)
    no_of_document = input(" \t[9] Enter No. Of Document:")
    L.append(no_of_document)
    customer_check_in = input(" \t[10] Enter Check In Date : ")
    L.append(customer_check_in)
    customer_check_out = input(" \t[11] Enter Check Out Date : ")
    L.append(customer_check_out)
    cust = (L)
    sql = "insert into customer_registration(customer_id, customer_name , customer_age , customer_sex ,customer_mobile_no , customer_email , customer_Nationality ,type_of_document, name_on_document , customer_no_of_document ,customer_check_in , check_out)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, cust)
    mydb.commit()
    print()
    print("[+] Customer Registration Completed Successfully. Your Customer ID is", customer_id)
    print("[+] Pls Remember Your Customer ID.")


def roombooking():
    L1 = []
    print(" \t---------------------------------------------------------------")
    print(" \t| no. Types  |            Description             |    Prices  |")
    print(" \t---------------------------------------------------------------")
    print(" \t| 1.| Single |   A room assigned to one person.   |   25000 Rs |")
    print(" \t| 2.| Double |   A room assigned to two people.   |   40000 Rs |")
    print(" \t| 3.| Triple |   A room assigned to three people. |   65000 Rs |")
    print(" \t| 4.| Quad   |   A room assigned to four people.  |   99000 Rs |")
    print(" \t| 5.| Queen  |   A room with a queen-sized bed.   |  125000 Rs |")
    print(" \t| 6.| King   |   A room with a king-sized bed.    |  150000 Rs |")
    print(" \t----------------------------------------------------------------")
    Customer_ID = int(input("Enter Customer ID: "))
    L1.append(Customer_ID)
    room_no = random.randint(101, 999)
    L1.append(room_no)
    room_choice = int(input("Enter Your Option: "))
    L1.append(room_choice)
    no_of_days = int(input("Enter No. Of Days: "))
    L1.append(no_of_days)
    if room_choice == 1:
        room_type = "Single Room"
        L1.append(room_type)
        room_rent = no_of_days * 25000
        L1.append(room_rent)
    elif room_choice == 2:
        room_type = "Double Room"
        L1.append(room_type)
        room_rent = no_of_days * 40000
        L1.append(room_rent)
    elif room_choice == 3:
        room_type = "Triple Room"
        L1.append(room_type)
        room_rent = no_of_days * 65000
        L1.append(room_rent)
    elif room_choice == 4:
        room_type = "Quad Room"
        L1.append(room_type)
        room_rent = no_of_days * 90000
        L1.append(room_rent)
    elif room_choice == 5:
        room_type = "Queen Room"
        L1.append(room_type)
        room_rent = no_of_days * 125000
        L1.append(room_rent)
    elif room_choice == 6:
        room_type = "King Room"
        L1.append(room_type)
        room_rent = no_of_days * 150000
        L1.append(room_rent)

    else:
        print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")

    roomrent = (L1)
    sql = "insert into Room_Booked(Customer_ID ,Room_No, Room_Choice , No_Of_Days , room_type, Room_Rent )values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, roomrent)
    mydb.commit()
    print()
    print("[+] Congratulations! Customer ", Customer_ID, " Your Room Has Booked At the Cost Of", room_rent)


def restaurant():
    L2 = []
    print()
    print("\t------------------------------------------------")
    print("\t| Sr.no |    Particular   |       Price        | ")
    print("\t------------------------------------------------")
    print("\t| 1.    |  Mutter Paneer  |   1300 Rs Per Dish | ")
    print("\t| 2.    |  Malai Kofta    |   1250 Rs Per Dish | ")
    print("\t| 3.    |  Palak Paneer   |   1450 Rs Per Dish | ")
    print("\t| 4.    |  Veg. Kolapuri  |   1500 Rs Per Dish | ")
    print("\t| 5.    |  Chicken Spicy  |   1800 Rs Per Dish | ")
    print("\t| 6.    | Chicken Special |   1900 Rs Per Dish | ")
    print("\t| 7.    |  Veg. pulao     |   1150 Rs Per Dish | ")
    print("\t| 8.    |  Veg. Briyani   |   1650 Rs Per Dish | ")
    print("\t| 9.    |  Veg. Combo     |   1750 Rs Per Dish | ")
    print("\t| 10.   |  Non Veg. Combo |   2500 Rs Per Dish | ")
    print("\t------------------------------------------------")
    Customer_ID = int(input("Enter Customer ID: "))
    L2.append(Customer_ID)
    choice_dish = int(input("Enter Choice: "))
    L2.append(choice_dish)
    quantity = int(input("Enter Quantity: "))
    L2.append(quantity)

    if choice_dish == 1:
        particular = "Mutter Paneer"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Mutter Paneer")
        restaurentbill = quantity * 1300

    elif choice_dish == 2:
        particular = "Malai Kofta"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Malai Kofta")
        restaurentbill = quantity * 1250

    elif choice_dish == 3:
        particular = "Palak Paneer"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Palak Paneer")
        restaurentbill = quantity * 1450
    elif choice_dish == 4:
        particular = "Veg. Kolapuri"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Veg. Kolapuri")
        restaurentbill = quantity * 1500
    elif choice_dish == 5:
        particular = "Chicken spicy"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Chicken spicy")
        restaurentbill = quantity * 1800
    elif choice_dish == 6:
        particular = "Chicken Special"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Chicken Special")
        restaurentbill = quantity * 1900
    elif choice_dish == 7:
        particular = "Veg. Pulao"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Veg. Pulao")
        restaurentbill = quantity * 1150
    elif choice_dish == 8:
        particular = "Biryani"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER:Biryani")
        restaurentbill = quantity * 1650
    elif choice_dish == 9:
        particular = "Vegetarian Combo"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Vegetarian Combo ")
        restaurentbill = quantity * 1750
    elif choice_dish == 10:
        particular = "Non-Vegetarian Combo"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Non-Vegetarian Combo ")
        restaurentbill = quantity * 2500

    else:
        print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!!")
    L2.append(restaurentbill)

    restaurant_bill = (L2)
    sql = "insert into restaurant_bill(Customer_ID ,choice_dish, quantity , Particular ,Total_Bill )values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql, restaurant_bill)
    mydb.commit()
    print()
    print("[+] We Hope You Will Enjoy Your Meal . Your Total Bill is ", restaurentbill)


def gamezone():
    L3 = []
    print("\t------------------------------------------------")
    print("\t| Sr.no |    Games        |       price        | ")
    print("\t------------------------------------------------")
    print("\t| 1.    |  Pin Ball       |   450 Rs per hour  | ")
    print("\t| 2.    |  Pac Man        |   700 Rs per hour  | ")
    print("\t| 3.    |  Mystery Room   |   1000 Rs per hour | ")
    print("\t| 4.    |  VR Games       |   1500 Rs per hour | ")
    print("\t------------------------------------------------")
    print()
    print("\tNOTE:Prices are according to one person")

    Customer_ID = int(input("Enter Customer ID: "))
    L3.append(Customer_ID)
    no_of_person = int(input("Enter No. of Person : "))
    L3.append(no_of_person)
    choice_game = int(input("Enter Choice: "))
    L3.append(choice_game)

    print()

    if choice_game == 1:
        game_name = "Pin Ball"
        L3.append(game_name)
        gzh = int(input("\tHow many hours would you like to play:"))
        total_bill = 450 * no_of_person * gzh
        L3.append(total_bill)

    elif choice_game == 2:
        game_name = "Pac Man"
        L3.append(game_name)
        gzh = int(input("\tHow many hours would you like to play:"))
        total_bill = 700 * no_of_person * gzh
        L3.append(total_bill)

    elif choice_game == 3:
        game_name = "Mystery Room"
        L3.append(game_name)
        gzh = int(input("\tHow many hours would you like to play:"))
        total_bill = 1000 * no_of_person * gzh
        L3.append(total_bill)

    elif choice_game == 4:
        game_name = "VR Games"
        L3.append(game_name)
        gzh = int(input("\tHow many hours would you like to play:"))
        total_bill = 1500 * no_of_person * gzh
        L3.append(total_bill)

    else:
        print("\tIt seems to be that you have entered the wrong number.")

    game_zone = (L3)
    sql = "insert into game_zone(Customer_ID , no_of_person, choice_game, name_of_game, Total_Bill )values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql, game_zone)
    mydb.commit()
    print()
    print("[+] We Hope You Will Enjoy Games . Your Total Bill for", game_name, "for", gzh, "Hours is", total_bill)


def shopping():
    L4 = []
    print("\t -------------------------------")
    print("\t |sr.no | items     |  price   |")
    print("\t |-----------------------------|")
    print("\t | 1.   | shirt     |  1500 Rs-|")
    print("\t | 2.   | t-shirt   |  2000 Rs-|")
    print("\t | 3.   | pant      |  3600 Rs-|")
    print("\t | 4.   | jacket    |  4500 Rs-|")
    print("\t -------------------------------")

    Customer_ID = int(input("Enter Customer ID: "))
    L4.append(Customer_ID)
    choice_particular = int(input("Enter Choice: "))
    L4.append(choice_particular)
    quantity = int(input("Enter Quantity : "))
    L4.append(quantity)

    print()

    if choice_particular == 1:
        particular_name = "Shirt"
        L4.append(particular_name)
        Total_Bill = 1500 * quantity
        L4.append(Total_Bill)

    elif choice_particular == 2:
        particular_name = "T-Shirt"
        L4.append(particular_name)
        total_bill = 2000 * quantity
        L4.append(total_bill)

    elif choice_particular == 3:
        particular_name = "Pant"
        L4.append(particular_name)
        total_bill = 3600 * quantity
        L4.append(total_bill)

    elif choice_particular == 4:
        particular_name = "Jacket"
        L4.append(particular_name)
        total_bill = 4500 * quantity
        L4.append(total_bill)

    else:
        print("\tIt seems to be that you have entered the wrong number.")

    shopping_zone = (L4)
    sql = "insert into shopping_zone(Customer_ID , choice_particular, quantity, particular_name, Total_Bill )values(%s,%s,%s,%s,%s)"
    mycursor.execute(sql, shopping_zone)
    mydb.commit()
    print()
    print("[+] We Hope You Have Enjoyed Your Shopping Time. The Total Bill for", quantity, "pieces of", particular_name,
          "is", total_bill)


# ************************* MYSQL MODIFICATION FUNCTIONS ************************* #
# ************************* VIEW DATABASE FUNCTIONS ************************* #

def registercust_sql():
    sql = "select * from customer_registration"
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


def restaurant_sql():
    sql = "select * from restaurant_bill"
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


def roombooking_sql():
    sql = "select * from room_booked"
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


def gamezone_sql():
    sql = "select * from game_zone"
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


def shopping_sql():
    sql = "select * from shopping_zone"
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


# ************************* UPDATE DATABASE ENTRIES FUNCTIONS ************************* #


def registercust_sql_update():
    L = []
    customer_id = input(" \t[0] Enter Customer ID: ")
    L.append(customer_id)
    customer_name = input(" \t[1] Enter Customer Name: ")
    L.append(customer_name)
    customer_age = int(input(" \t[2] Enter Age: "))
    L.append(customer_age)
    customer_sex = input(" \t[3] Enter Sex: ")
    L.append(customer_sex)
    customer_moblie_no = input(" \t[4] Enter Mobile no.: ")
    L.append(customer_moblie_no)
    customer_email = input(" \t[5] Enter Email: ")
    L.append(customer_email)
    customer_Nationality = input(" \t[6] Enter Nationality: ")
    L.append(customer_Nationality)
    type_of_document = input(" \t[7] Enter Type Of Document: ")
    L.append(type_of_document)
    name_on_document = input(" \t[8] Enter Name On Document: ")
    L.append(name_on_document)
    no_of_document = input(" \t[9] Enter No. Of Document:")
    L.append(no_of_document)
    customer_check_in = input(" \t[10] Enter Check In Date : ")
    L.append(customer_check_in)
    customer_check_out = input(" \t[11] Enter Check Out Date : ")
    L.append(customer_check_out)
    cust = (L)
    sql = '''insert into customer_registration(customer_id, customer_name , 
    customer_age , customer_sex ,customer_mobile_no , customer_email , customer_Nationality ,
    type_of_document, name_on_document , customer_no_of_document ,customer_check_in , check_out
    )values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE customer_name = VALUES(customer_name),customer_age = VALUES(customer_age),
    customer_sex = VALUES(customer_sex), customer_mobile_no = VALUES(customer_mobile_no),
    customer_email = VALUES(customer_email), customer_Nationality = VALUES(customer_Nationality), type_of_document = VALUES(type_of_document)
    , name_on_document = VALUES(name_on_document),customer_no_of_document = VALUES(customer_no_of_document), customer_check_in = VALUES(customer_check_in),
    check_out = VALUES(check_out)'''
    mycursor.execute(sql, cust)
    mydb.commit()
    print()
    print("[+] Customer Registration Completed Successfully.")


def roombooking_sql_update():
    L1 = []
    print(" \t---------------------------------------------------------------")
    print(" \t| no. Types  |            Description             |    Prices  |")
    print(" \t---------------------------------------------------------------")
    print(" \t| 1.| Single |   A room assigned to one person.   |   25000 Rs |")
    print(" \t| 2.| Double |   A room assigned to two people.   |   40000 Rs |")
    print(" \t| 3.| Triple |   A room assigned to three people. |   65000 Rs |")
    print(" \t| 4.| Quad   |   A room assigned to four people.  |   99000 Rs |")
    print(" \t| 5.| Queen  |   A room with a queen-sized bed.   |  125000 Rs |")
    print(" \t| 6.| King   |   A room with a king-sized bed.    |  150000 Rs |")
    print(" \t----------------------------------------------------------------")
    Customer_ID = int(input("Enter Customer ID: "))
    L1.append(Customer_ID)
    room_no = random.randint(101, 999)
    L1.append(room_no)
    room_choice = int(input("Enter Your Option: "))
    L1.append(room_choice)
    no_of_days = int(input("Enter No. Of Days: "))
    L1.append(no_of_days)
    if room_choice == 1:
        room_type = "Single Room"
        L1.append(room_type)
        room_rent = no_of_days * 25000
        L1.append(room_rent)
    elif room_choice == 2:
        room_type = "Double Room"
        L1.append(room_type)
        room_rent = no_of_days * 40000
        L1.append(room_rent)
    elif room_choice == 3:
        room_type = "Triple Room"
        L1.append(room_type)
        room_rent = no_of_days * 65000
        L1.append(room_rent)
    elif room_choice == 4:
        room_type = "Quad Room"
        L1.append(room_type)
        room_rent = no_of_days * 90000
        L1.append(room_rent)
    elif room_choice == 5:
        room_type = "Queen Room"
        L1.append(room_type)
        room_rent = no_of_days * 125000
        L1.append(room_rent)
    elif room_choice == 6:
        room_type = "King Room"
        L1.append(room_type)
        room_rent = no_of_days * 150000
        L1.append(room_rent)

    else:
        print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")

    roomrent = (L1)
    sql = '''insert into Room_Booked(Customer_ID ,
    Room_No, Room_Choice , No_Of_Days , room_type,
    Room_Rent )values(%s,%s,%s,%s,%s,%s) 
    ON DUPLICATE KEY UPDATE Room_No = VALUES(Room_No),Room_choice = VALUES(Room_choice),
    No_Of_Days = VALUES(No_Of_Days), room_type = VALUES(room_type),
    Room_Rent = VALUES(Room_Rent)'''
    mycursor.execute(sql, roomrent)
    mydb.commit()
    print()
    print("[+] Congratulations! Customer ", Customer_ID, " Your Room Has Booked At the Cost Of", room_rent)


def restaurant_sql_update():
    L2 = []
    Customer_ID = int(input("Enter Customer ID: "))
    L2.append(Customer_ID)
    choice_dish = int(input("Enter Choice: "))
    L2.append(choice_dish)
    quantity = int(input("Enter Quantity: "))
    L2.append(quantity)

    if choice_dish == 1:
        particular = "Mutter Paneer"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Mutter Paneer")
        restaurentbill = quantity * 300

    elif choice_dish == 2:
        particular = "Malai Kofta"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Malai Kofta")
        restaurentbill = quantity * 250

    elif choice_dish == 3:
        particular = "Palak Paneer"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Palak Paneer")
        restaurentbill = quantity * 450
    elif choice_dish == 4:
        particular = "Veg. Kolapuri"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Veg. Kolapuri")
        restaurentbill = quantity * 500
    elif choice_dish == 5:
        particular = "Chicken spicy"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Chicken spicy")
        restaurentbill = quantity * 800
    elif choice_dish == 6:
        particular = "Chicken Special"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Chicken Special")
        restaurentbill = quantity * 900
    elif choice_dish == 7:
        particular = "Veg. Pulao"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Veg. Pulao")
        restaurentbill = quantity * 150
    elif choice_dish == 8:
        particular = "Biryani"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER:Biryani")
        restaurentbill = quantity * 650
    elif choice_dish == 9:
        particular = "Vegetarian Combo"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Vegetarian Combo ")
        restaurentbill = quantity * 750
    elif choice_dish == 10:
        particular = "Non-Vegetarian Combo"
        L2.append(particular)
        print("\nSO YOU HAVE ORDER: Non-Vegetarian Combo ")
        restaurentbill = quantity * 1200

    else:
        print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!!")
    L2.append(restaurentbill)

    restaurant_bill = (L2)
    sql = '''insert into restaurant_bill(Customer_ID ,choice_dish, quantity , Particular ,Total_Bill )values(%s,%s,%s,%s,%s) 
    ON DUPLICATE KEY UPDATE choice_dish = VALUES(choice_dish),quantity = VALUES(quantity),
    Particular = VALUES(Particular), Total_Bill = VALUES(Total_Bill)'''
    mycursor.execute(sql, restaurant_bill)
    mydb.commit()
    print()
    print("[+] We Hope You Will Enjoy Your Meal . Your Total Bill is ", restaurentbill)


def gamezone_sql_update():
    L3 = []
    print("\t------------------------------------------------")
    print("\t| Sr.no |    Games        |       price        | ")
    print("\t------------------------------------------------")
    print("\t| 1.    |  Pin Ball       |   450 Rs per hour  | ")
    print("\t| 2.    |  Pac Man        |   700 Rs per hour  | ")
    print("\t| 3.    |  Mystery Room   |   1000 Rs per hour | ")
    print("\t| 4.    |  VR Games       |   1500 Rs per hour | ")
    print("\t------------------------------------------------")
    print()
    print("\tNOTE:Prices are according to one person")

    Customer_ID = int(input("Enter Customer ID: "))
    L3.append(Customer_ID)
    no_of_person = int(input("Enter No. of Person : "))
    L3.append(no_of_person)
    choice_game = int(input("Enter Choice: "))
    L3.append(choice_game)

    print()

    if choice_game == 1:
        game_name = "Pin Ball"
        L3.append(game_name)
        gzh = int(input("\tHow many hours would you like to play:"))
        total_bill = 450 * no_of_person * gzh
        L3.append(total_bill)

    elif choice_game == 2:
        game_name = "Pac Man"
        L3.append(game_name)
        gzh = int(input("\tHow many hours would you like to play:"))
        total_bill = 700 * no_of_person * gzh
        L3.append(total_bill)

    elif choice_game == 3:
        game_name = "Mystery Room"
        L3.append(game_name)
        gzh = int(input("\tHow many hours would you like to play:"))
        total_bill = 1000 * no_of_person * gzh
        L3.append(total_bill)

    elif choice_game == 4:
        game_name = "VR Games"
        L3.append(game_name)
        gzh = int(input("\tHow many hours would you like to play:"))
        total_bill = 1500 * no_of_person * gzh
        L3.append(total_bill)

    else:
        print("\tIt seems to be that you have entered the wrong number.")

    game_zone = (L3)
    sql = '''insert into game_zone(Customer_ID , no_of_person, choice_game, name_of_game, Total_Bill )values(%s,%s,%s,%s,%s) 
    ON DUPLICATE KEY UPDATE no_of_person = VALUES(no_of_person),choice_game = VALUES(choice_game),
    name_of_game = VALUES(name_of_game), Total_Bill = VALUES(Total_Bill)'''
    mycursor.execute(sql, game_zone)
    mydb.commit()
    print()
    print("[+] We Hope You Will Enjoy Games . Your Total Bill for", game_name, "for", gzh, "Hours is", total_bill)


def shopping_sql_update():
    L4 = []
    print("\t -------------------------------")
    print("\t |sr.no | items     |  price   |")
    print("\t |-----------------------------|")
    print("\t | 1.   | shirt     |  1500 Rs-|")
    print("\t | 2.   | t-shirt   |  2000 Rs-|")
    print("\t | 3.   | pant      |  3600 Rs-|")
    print("\t | 4.   | jacket    |  4500 Rs-|")
    print("\t -------------------------------")

    Customer_ID = int(input("Enter Customer ID: "))
    L4.append(Customer_ID)
    choice_particular = int(input("Enter Choice: "))
    L4.append(choice_particular)
    quantity = int(input("Enter Quantity : "))
    L4.append(quantity)

    print()

    if choice_particular == 1:
        particular_name = "Shirt"
        L4.append(particular_name)
        Total_Bill = 450 * quantity
        L4.append(Total_Bill)

    elif choice_particular == 2:
        particular_name = "T-Shirt"
        L4.append(particular_name)
        total_bill = 700 * quantity
        L4.append(total_bill)

    elif choice_particular == 3:
        particular_name = "Pant"
        L4.append(particular_name)
        total_bill = 1000 * quantity
        L4.append(total_bill)

    elif choice_particular == 4:
        particular_name = "Jacket"
        L4.append(particular_name)
        total_bill = 1500 * quantity
        L4.append(total_bill)

    else:
        print("\tIt seems to be that you have entered the wrong number.")

    shopping_zone = (L4)
    sql = '''insert into shopping_zone(Customer_ID , choice_particular, quantity, particular_name, Total_Bill )values(%s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE choice_particular = VALUES(choice_particular),quantity = VALUES(quantity),
    particular_name = VALUES(particular_name), Total_Bill = VALUES(Total_Bill)'''
    mycursor.execute(sql, shopping_zone)
    mydb.commit()
    print()
    print("[+] We Hope You Have Enjoyed Your Shopping Time. The Total Bill for", quantity, "pieces of", particular_name,
          "is", total_bill)


# ************************* DELETE DATABASE ENTRIES FUNCTIONS ************************* #


def roombooking_sql_delete():
    customer_id = input("Enter Customer ID: ")
    sql = "DELETE FROM room_booked WHERE customer_id =" + customer_id
    mycursor.execute(sql, customer_id)
    mydb.commit()
    print("Record of Id=", customer_id, "has been deleted successfully")


def registercust_sql_delete():
    customer_id = input("Enter Customer ID: ")
    sql = "DELETE FROM customer_registration WHERE customer_id=" + customer_id
    mycursor.execute(sql, customer_id)
    mydb.commit()
    print("Record of Id=", customer_id, "has been deleted successfully")


def restaurant_sql_delete():
    customer_id = input("Enter Customer ID: ")
    sql = "DELETE FROM restaurant_bill WHERE customer_id= " + customer_id
    mycursor.execute(sql, customer_id)
    mydb.commit()
    print("Record of Id=", customer_id, "has been deleted successfully")


def gamezone_sql_delete():
    customer_id = input("Enter Customer ID: ")
    sql = "DELETE FROM game_zone WHERE customer_id= " + customer_id
    mycursor.execute(sql, customer_id)
    mydb.commit()
    print("Record of Id=", customer_id, "has been deleted successfully")


def shopping_sql_delete():
    customer_id = input("Enter Customer ID: ")
    sql = "DELETE FROM shopping_zone WHERE customer_id= " + customer_id
    mycursor.execute(sql, customer_id)
    mydb.commit()
    print("Record of Id=", customer_id, "has been deleted successfully")


# ************************* SEARCH DATABASE ENTRIES FUNCTIONS ************************* #


def registercust_sql_search():
    customer_id = input("Enter Customer Id:- ")
    sql = "SELECT * FROM customer_registration WHERE customer_id=" + customer_id
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


def roombooking_sql_search():
    customer_id = input("Enter Customer Id:- ")
    sql = "SELECT * FROM room_booked WHERE customer_id=" + customer_id
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


def restaurant_sq_search():
    customer_id = input("Enter Customer Id:- ")
    sql = "SELECT * FROM restaurant_bill WHERE customer_id=" + customer_id
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


def gamezone_sq_searchl():
    customer_id = input("Enter Customer Id:- ")
    sql = "SELECT * FROM game_zone WHERE customer_id=" + customer_id
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


def shopping_sql_search():
    customer_id = input("Enter Customer Id:- ")
    sql = "SELECT * FROM shopping_zone WHERE customer_id=" + customer_id
    result_d = pd.read_sql(sql, mydb)
    print(result_d)


# ************************* BILLING FUNCTIONS ************************* #

def final_bill():
    l = []
    date_now = datetime.datetime.now()
    l.append(date_now)

    customer_id = input("Enter Customer Id:- ")
    l.append(customer_id)

    sql = "select customer_name from customer_registration where customer_id = " + customer_id
    f_b = mycursor.execute(sql)
    name_fb = mycursor.fetchone()
    i = 1
    for i in name_fb:
        name_fb_1 = i
    l.append(name_fb_1)

    sql = "select customer_mobile_no from customer_registration where customer_id = " + customer_id
    m_n = mycursor.execute(sql)
    mobile_mn = mycursor.fetchone()
    i = 1
    for i in mobile_mn:
        mobile_mn_1 = i
    l.append(mobile_mn_1)

    sql = "select Room_No from room_booked where customer_id = " + customer_id
    rm = mycursor.execute(sql)
    r_n = mycursor.fetchone()
    i = 1
    for i in r_n:
        r_n_1 = i
    l.append(r_n_1)

    sql = "select No_of_Days from room_booked where customer_id = " + customer_id
    n_d = mycursor.execute(sql)
    no_days = mycursor.fetchone()
    i = 1
    for i in no_days:
        no_days_1 = i
    l.append(no_days_1)

    sql = "select sum(Room_Rent) from room_booked where Customer_ID = " + customer_id
    r_bo = mycursor.execute(sql)
    Totalbill_RBO = mycursor.fetchone()
    i = 1
    for i in Totalbill_RBO:
        bill_rbo = i
    l.append(bill_rbo)

    sql = "select sum(Total_Bill) from restaurant_bill where Customer_ID = " + customer_id
    r_b = mycursor.execute(sql)
    Totalbill_RB = mycursor.fetchone()
    i = 1
    for i in Totalbill_RB:
        bill_rb = i
    l.append(bill_rb)

    sql = "select sum(Total_Bill) from shopping_zone where Customer_ID = " + customer_id
    s_z = mycursor.execute(sql)
    Totalbill_SZ = mycursor.fetchone()
    i = 1
    for i in Totalbill_SZ:
        bill_sz = i
    l.append(bill_sz)

    sql = "select sum(Total_Bill) from game_zone where Customer_ID = " + customer_id
    g_z = mycursor.execute(sql)
    Totalbill_GZ = mycursor.fetchone()
    i = 1
    for i in Totalbill_GZ:
        bill_gz = i
    l.append(bill_gz)

    print()
    print("---------------------------- The Soho Palace ----------------------------")
    print("------------------ 261 Street, Gangtok, India - 737101 ------------------")
    print()
    print("\t        Billing Date : ", date_now.day, "/", date_now.month, "/", date_now.year)
    print("\tCustomer Room Number : ", r_n_1)
    print("\t         Customer id : ", customer_id)
    print("\t             Name    : ", name_fb_1)
    print("\t          Mobile no. : ", mobile_mn_1)
    print("\t   Total no. of days : ", no_days_1, "Days")
    print()
    #float_rbo = float(bill_rbo)
    total_bill = bill_gz + bill_rb + bill_rb + bill_rbo
    l.append(total_bill)
    print("\t-----------------------------------------------------------------------")
    print("\tSr.no                 Particular                    Price")
    print("\t-----------------------------------------------------------------------")
    print("\t 1                    Room Rent                    ", bill_rbo, "Rs")
    print("\t 2                    Restaurant bill              ", bill_rb, "Rs")
    print("\t 3                    Gaming Zone bill             ", bill_gz, "Rs")
    print("\t 4                    Shopping Zone bill           ", bill_sz, "Rs")
    print("\t-----------------------------------------------------------------------")
    print("\t                      Total                        ", total_bill, "Rs")
    print("\t-----------------------------------------------------------------------")
    print()
    print("\tOutstanding payment : ", total_bill, "Rs")
    print()
    payment = input("\tEnter Payment mode : ")
    l.append(payment)
    print("Loading..Pls Wait..")
    time.sleep(3)
    status = "[+] Payment Done Successfully"
    l.append(status)
    print(status)
    print("Thank You!! Visit Again!! ")

    cust = (l)
    sql = "insert into final_bill(date_now,customer_id,name_fb_1,mobile_mn_1,r_n_1,no_days_1,bill_rbo,bill_rb,bill_gz,bill_sz,total_bill,payment_type,status)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, cust)
    mydb.commit()


def previous_bills():
    customer_id = input("Enter Customer Id:- ")
    sql = "select sum(Room_Rent) from room_booked where Customer_ID = " + customer_id
    r_bo = mycursor.execute(sql)
    Totalbill_RBO = mycursor.fetchone()
    i = 1
    for i in Totalbill_RBO:
        bill_rbo = i

    sql = "select sum(Total_Bill) from restaurant_bill where Customer_ID = " + customer_id
    r_b = mycursor.execute(sql)
    Totalbill_RB = mycursor.fetchone()
    i = 1
    for i in Totalbill_RB:
        bill_rb = i

    sql = "select sum(Total_Bill) from shopping_zone where Customer_ID = " + customer_id
    s_z = mycursor.execute(sql)
    Totalbill_SZ = mycursor.fetchone()
    i = 1
    for i in Totalbill_SZ:
        bill_sz = i

    sql = "select sum(Total_Bill) from game_zone where Customer_ID = " + customer_id
    g_z = mycursor.execute(sql)
    Totalbill_GZ = mycursor.fetchone()
    i = 1
    for i in Totalbill_GZ:
        bill_gz = i

    sql = "select customer_name from customer_registration where customer_id = " + customer_id
    f_b = mycursor.execute(sql)
    name_fb = mycursor.fetchone()
    i = 1
    for i in name_fb:
        name_fb_1 = i

    sql = "select customer_mobile_no from customer_registration where customer_id = " + customer_id
    m_n = mycursor.execute(sql)
    mobile_mn = mycursor.fetchone()
    i = 1
    for i in mobile_mn:
        mobile_mn_1 = i

    sql = "select Room_No from room_booked where customer_id = " + customer_id
    rm = mycursor.execute(sql)
    r_n = mycursor.fetchone()
    i = 1
    for i in r_n:
        r_n_1 = i

    sql = "select No_of_Days from room_booked where customer_id = " + customer_id
    n_d = mycursor.execute(sql)
    no_days = mycursor.fetchone()
    i = 1
    for i in no_days:
        no_days_1 = i

    sql = "select date_now from final_bill where customer_id = " + customer_id
    d = mycursor.execute(sql)
    date = mycursor.fetchone()
    i = 1
    for i in date:
        date_1 = i

    print()
    print("---------------------------- The Soho Palace ----------------------------")
    print("------------------ 261 Street, Gangtok, India - 737101 ------------------")
    print()
    print("\t        Billing Date : ", date_1)
    print("\tCustomer Room Number : ", r_n_1)
    print("\t         Customer id : ", customer_id)
    print("\t             Name    : ", name_fb_1)
    print("\t          Mobile no. : ", mobile_mn_1)
    print("\t   Total no. of days : ", no_days_1, "Days")
    print()
    #float_rbo = float(bill_rbo)
    total_bill = bill_gz + bill_rb + bill_rb + bill_rbo
    print("\t-----------------------------------------------------------------------")
    print("\tSr.no                 Particular                    Price")
    print("\t-----------------------------------------------------------------------")
    print("\t 1                    Room Rent                    ", bill_rbo, "Rs")
    print("\t 2                    Restaurant bill              ", bill_rb, "Rs")
    print("\t 3                    Gaming Zone bill             ", bill_gz, "Rs")
    print("\t 4                    Shopping Zone bill           ", bill_sz, "Rs")
    print("\t-----------------------------------------------------------------------")
    print("\t                      Total                        ", total_bill, "Rs")
    print("\t-----------------------------------------------------------------------")
    print()
    print("\tPaid Amount : ", total_bill, "Rs")
    print()


# ************************* Sales Graph Analysis ************************* #


def restaurant_sales_graph () :
    mycursor.execute("select quantity from restaurant_bill where choice_dish = 1")
    ch1 = mycursor.fetchall()
    choi1 = []
    for i in ch1:
        choi1.append(i[0])
    choice_1 = sum(choi1)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 2")
    ch2 = mycursor.fetchall()
    choi2 = []
    for i in ch2:
        choi2.append(i[0])
    choice_2 = sum(choi2)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 3")
    ch3 = mycursor.fetchall()
    choi3 = []
    for i in ch3:
        choi3.append(i[0])
    choice_3 = sum(choi3)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 4")
    ch4 = mycursor.fetchall()
    choi4 = []
    for i in ch2:
        choi4.append(i[0])
    choice_4 = sum(choi4)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 5")
    ch5 = mycursor.fetchall()
    choi5 = []
    for i in ch5:
        choi5.append(i[0])
    choice_5 = sum(choi5)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 6")
    ch6 = mycursor.fetchall()
    choi6 = []
    for i in ch6:
        choi6.append(i[0])
    choice_6 = sum(choi6)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 7")
    ch7 = mycursor.fetchall()
    choi7 = []
    for i in ch7:
        choi7.append(i[0])
    choice_7 = sum(choi7)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 8")
    ch8 = mycursor.fetchall()
    choi8 = []
    for i in ch8:
        choi8.append(i[0])
    choice_8 = sum(choi8)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 9")
    ch9 = mycursor.fetchall()
    choi9 = []
    for i in ch9:
        choi9.append(i[0])
    choice_9 = sum(choi9)

    mycursor.execute("select quantity from restaurant_bill where choice_dish = 10")
    ch10 = mycursor.fetchall()
    choi10 = []
    for i in ch10:
        choi10.append(i[0])
    choice_10 = sum(choi10)

    particulars = ["Mutter Paneer", "Malai Kofta", "Palak Paneer", "Veg. Kolapuri", "Chicken Spicy", "Chicken Special",
                   "Veg. Pulao", "Veg. Briyani", "Veg. Combo", "Non Veg. Combo"]
    quantity = [choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8, choice_9, choice_10]
    plt.figure(figsize=(16, 5))
    plt.title("Restaurant Sales")
    plt.xlabel("Types Of Dishes")
    plt.ylabel("Quantity Sales")
    plt.bar(particulars, quantity)
    plt.show()


def game_zone_sales_graph () :
    mycursor.execute("select no_of_person from game_zone where choice_game = 1")
    ch1 = mycursor.fetchall()
    choi1 = []
    for i in ch1:
        choi1.append(i[0])
    choice_1 = sum(choi1)

    mycursor.execute("select no_of_person from game_zone where choice_game = 2")
    ch2 = mycursor.fetchall()
    choi2 = []
    for i in ch2:
        choi2.append(i[0])
    choice_2 = sum(choi2)

    mycursor.execute("select no_of_person from game_zone where choice_game = 3")
    ch3 = mycursor.fetchall()
    choi3 = []
    for i in ch3:
        choi3.append(i[0])
    choice_3 = sum(choi3)

    mycursor.execute("select no_of_person from game_zone where choice_game = 4")
    ch4 = mycursor.fetchall()
    choi4 = []
    for i in ch4:
        choi4.append(i[0])
    choice_4 = sum(choi4)

    particulars = ["Pin Ball", "Pac Man","Mystery Room","VR Games"]
    quantity = [choice_1, choice_2, choice_3, choice_4]
    plt.figure(figsize=(8, 5))
    plt.title("Game Zone Sales")
    plt.xlabel("Types Of Games")
    plt.ylabel("Quantity Sales")
    plt.bar(particulars, quantity)
    plt.show()


def shopping_zone_garph ():
    mycursor.execute("select quantity from shopping_zone where choice_particular = 1")
    ch1 = mycursor.fetchall()
    choi1 = []
    for i in ch1:
        choi1.append(i[0])
    choice_1 = sum(choi1)

    mycursor.execute("select quantity from shopping_zone where choice_particular = 2")
    ch2 = mycursor.fetchall()
    choi2 = []
    for i in ch2:
        choi2.append(i[0])
    choice_2 = sum(choi2)

    mycursor.execute("select quantity from shopping_zone where choice_particular = 3")
    ch3 = mycursor.fetchall()
    choi3 = []
    for i in ch3:
        choi3.append(i[0])
    choice_3 = sum(choi3)

    mycursor.execute("select quantity from shopping_zone where choice_particular = 4")
    ch4 = mycursor.fetchall()
    choi4 = []
    for i in ch4:
        choi4.append(i[0])
    choice_4 = sum(choi4)

    particulars = ["Shirt", "T-Shirt", "Pant", "Jacket"]
    quantity = [choice_1, choice_2, choice_3, choice_4]
    plt.figure(figsize=(8, 5))
    plt.title("Shopping Zone Sales")
    plt.xlabel("Types Of Garments")
    plt.ylabel("Quantity Sales")
    plt.bar(particulars, quantity)
    plt.show()


# ************************* MULTI FUNCTIONAL LOOPED MENU  ************************* #

def Main_MenuSet():
    auto_table_creation()
    print()
    intro()
    print()

    def final_menu():
        print("| [1] | New Registration                     ")
        print("| [2] | Previous Data & Modification Of Data ")
        print("| [3] | Sales Graph Analysis                 ")
        print("| [0] | Exit The Program                     ")

    final_menu()
    option = int(input("Enter Your Option: "))
    while option != 0:
        if option == 1:
            def menu_python():
                print("| [1] | Customer Registration")
                print("| [2] | Room Booking")
                print("| [3] | Restaurant")
                print("| [4] | Game Zone")
                print("| [5] | Shopping Zone")
                print("| [6] | Final Bill")
                print("| [0] | Exit the program.")

            menu_python()
            option = int(input("Enter Your Option: "))
            while option != 0:
                if option == 1:
                    registercust()
                elif option == 2:
                    roombooking()
                elif option == 3:
                    restaurant()
                elif option == 4:
                    gamezone()
                elif option == 5:
                    shopping()
                elif option == 6:
                    final_bill()
                elif option == 0:
                    break
                else:
                    print("Thank You !!")
                print()
                menu_python()
                option = int(input("Enter Your Option: "))
        elif option == 2:
            def menu_sql():
                print("Info : [1] - [5]  :  Previous Data")
                print("Info : [6] - [9]  :  Modification Data")
                print("| [1] | Customer Registration Data")
                print("| [2] | Room Booking Data")
                print("| [3] | Restaurant Data")
                print("| [4] | Game Zone Data")
                print("| [5] | shopping Zone Data")
                print("| [6] | Search ")
                print("| [7] | Updation Of Data")
                print("| [8] | Removal Of Data")
                print("| [9] | Previous Bills")
                print("| [0] | Exit the program.")

            menu_sql()
            option = int(input("Enter Your Option: "))
            while option != 0:
                if option == 1:
                    registercust_sql()
                elif option == 2:
                    roombooking_sql()
                elif option == 3:
                    restaurant_sql()
                elif option == 4:
                    gamezone_sql()
                elif option == 5:
                    shopping_sql()
                elif option == 6:
                    def menu_sql_search():
                        print("| [1] | Customer Registration Data")
                        print("| [2] | Room Booking Data")
                        print("| [3] | Restaurant Data")
                        print("| [4] | Game Zone Data")
                        print("| [5] | shopping Zone Data")
                        print("| [0] | Exit the program.")

                    menu_sql_search()
                    option = int(input("Enter Your Option: "))

                    while option != 0:
                        if option == 1:
                            registercust_sql_search()
                        elif option == 2:
                            roombooking_sql_search()
                        elif option == 3:
                            restaurant_sq_search()
                        elif option == 4:
                            gamezone_sq_searchl()
                        elif option == 5:
                            shopping_sql_search()
                        elif option == 0:
                            break
                        else:
                            print("Thank You !!")
                        print()
                        menu_sql_search()
                        option = int(input("Enter Your Option: "))
                elif option == 7:
                    def menu_sql_update():
                        print("| [1] | Customer Registration Data")
                        print("| [2] | Room Booking Data")
                        print("| [3] | Restaurant Data")
                        print("| [4] | Game Zone Data")
                        print("| [5] | shopping Zone Data")
                        print("| [0] | Exit the program.")

                    menu_sql_update()
                    option = int(input("Enter Your Option: "))

                    while option != 0:
                        if option == 1:
                            registercust_sql_update()
                        elif option == 2:
                            roombooking_sql_update()
                        elif option == 3:
                            restaurant_sql_update()
                        elif option == 4:
                            gamezone_sql_update()
                        elif option == 5:
                            shopping_sql_update()
                        elif option == 0:
                            break
                        else:
                            print("Thank You !!")
                        print()
                        menu_sql_update()
                        option = int(input("Enter Your Option: "))
                elif option == 8:
                    def menu_sql_update():
                        print("| [1] | Customer Registration Data")
                        print("| [2] | Room Booking Data")
                        print("| [3] | Restaurant Data")
                        print("| [4] | Game Zone Data")
                        print("| [5] | shopping Zone Data")
                        print("| [0] | Exit the program.")

                    menu_sql_update()
                    option = int(input("Enter Your Option: "))

                    while option != 0:
                        if option == 1:
                            registercust_sql_delete()
                        elif option == 2:
                            roombooking_sql_delete()
                        elif option == 3:
                            restaurant_sql_delete()
                        elif option == 4:
                            gamezone_sql_delete()
                        elif option == 5:
                            shopping_sql_delete()
                        elif option == 0:
                            break
                        else:
                            print("Thank You !!")
                        print()
                        menu_sql_update()
                        option = int(input("Enter Your Option: "))
                elif option == 9:
                    previous_bills()
                    break
                elif option == 0:
                    break
                else :
                    print("Thank You")
                print()
                menu_sql()
                option = int(input("Enter Your Option: "))
        elif option == 3 :
            def sales_graph():
                print("| [1] | Restaurant Sales Graph")
                print("| [2] | Game Zone Sales Graph")
                print("| [3] | Shopping Zone Sales Graph")
                print("| [0] | Exit")

            sales_graph()
            option = int(input("Enter Your Option: "))
            while option != 0:
                if option == 1:
                    restaurant_sales_graph()
                elif option == 2:
                    game_zone_sales_graph()
                elif option == 3:
                    shopping_zone_garph()
                elif option == 0:
                    break
                else:
                    print("Thank You !!")
                print()
                sales_graph()
                option = int(input("Enter Your Option: "))
        else:
            break
        print()
        final_menu()
        option = int(input("Enter Your Option: "))


Main_MenuSet()

# ************************* END OF PROJECT ************************* #
