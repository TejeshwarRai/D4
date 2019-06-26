import mysql.connector

class DBHelper:

    def saveCustomerInDB(self, customer):
        sql = "Insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
        con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "aur01")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

class customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print(">>Name: {} Phone: {} Email:{}".format(self.name, self.phone, self.email))

print("Options: ")
print("1. Create New Customer: ")

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