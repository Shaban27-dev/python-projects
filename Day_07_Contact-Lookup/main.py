#          DAY-7
# Contact Book (store name, phone, email).
def Shaban():
    info = {
        "name": "Shaban",
        "phone": "8394829812",
        "email": "alamshaban92@gmail.com",
    }
    return info

def Sarib():
    info = {
        "name": "Ssrib",
        "phone": "8394893021",
        "email": "sarib29@gmail.com",
    }
    return info

def James():
    info = {
        "name": "James",
        "phone": "9203129812",
        "email": "jamesclear40@gmail.com",
    }
    return info

def Bob():
    info = {
        "name": "Bob",
        "phone": "8399021812",
        "email": "bobshane853@gmail.com",
    }
    return info

people = {
    "shaban": Shaban,
    "sarib": Sarib,
    "james": James,
    "bob": Bob,
}

ask = input("Who do you want to know about? 'Shaban', 'Sarib', 'James', or 'Bob': ").lower()
if ask in people:
    print(people[ask]())
else:
    print("Sorry, I don't have info of that person.")