import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print(">>Name: {} Phone: {} Email:{}".format(self.name, self.phone, self.email))


# Use a service account
cred = credentials.Certificate('C:/Users/dell/Desktop/Auribises/D4/venv/AurDem01.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection("customer").stream()
for doc in docs:
    print(doc.id, doc.to_dict())
print("k")