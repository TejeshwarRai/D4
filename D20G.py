from tkinter import *

from D19 import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:/Users/dell/Desktop/Auribises/D4/venv/AurDem01.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

window = Tk()
def onClick():
    print("Button Clicked")
    cRef = customer(None,None,None)
    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()
    cRef.showCustomerDetails()
    data = cRef.__dict__
    db.collection("customer").document().set(data)
    print("Saved in Firebase")

lblTitle = Label(window, text="Add Customer Details")
lblTitle.pack()


lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblName = Label(window, text="Enter Customer Phone")
lblName.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblName = Label(window, text="Enter Customer Email")
lblName.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()


window.mainloop()