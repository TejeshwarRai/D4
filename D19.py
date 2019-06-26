import mysql.connector

class DBHelper:


    def saveCustomerInDB(self, customer):
        sql = "Insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
        con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "aur01")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

    def UpdateCustomerInDB(self, customer):
        sql = "update customer set name = '{}',phone = '{}',email =  '{}' where cid = {}".format(customer.name, customer.phone, customer.email, customer.cid)
        con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "aur01")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

    def DeleteCustomerInDB(self,cid):
        sql = "delete from customer where cid = {}".format(cid)
        con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "aur01")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()


    def fetchAll(self):
        sql = "select * from customer"
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="aur01")
        cursor = con.cursor()
        cursor.execute(sql)

class customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print(">>Name: {} Phone: {} Email:{}".format(self.name, self.phone, self.email))

"""
print("Options: ")
print("1. Create New Customer: ")
print("2. Update Customer: ")
print("3. Delete Customer: ")
print(("4. View Data"))
choice = int(input("Enter Choice: "))

if choice == 1:
    cRef = customer(None, None, None)
    cRef.name = input("Enter Customer Name: ")
    cRef.phone = input("Enter Customer Phone: ")
    cRef.email = input("Enter Customer Email: ")

    cRef.showCustomerDetails()

    save = input("Would you like to save:")
    if save == "yes":
        db = DBHelper()
        db.saveCustomerInDB(cRef)
        print("Saved!!!!")
    else:
        print("Exiting")
        exit()

if choice == 2:
    cRef = customer(None, None, None)
    cRef.cid = int(input("Enter cid: "))
    cRef.name = input("Enter Customer Name: ")
    cRef.phone = input("Enter Customer Phone: ")
    cRef.email = input("Enter Customer Email: ")

    # cRef.showCustomerDetails()

    save = input("Would you like to update:")
    if save == "yes":
        db = DBHelper()
        db.UpdateCustomerInDB(cRef)
        print("Updated!!!!")
    else:
        print("Exiting")
        exit()

if choice == 3:
    cid = int(input("Enter cid: "))
    save = input("Would you like to delete:")

    if save == "yes":
        db = DBHelper()
        db.DeleteCustomerInDB(cid)
        print("Deleted!!!!")
    else:
        print("Exiting")
        exit()

if choice == 4:
    cid = int(input("Enter cid: "))
    save = input("Would you like to delete:")

    if save == "yes":
        db = DBHelper()
        db.DeleteCustomerInDB(cid)
        print("Deleted!!!!")
    else:
        print("Exiting")
        exit()
"""