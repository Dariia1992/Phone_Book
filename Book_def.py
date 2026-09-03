
import csv




my_phone_b = {
    "Anna": {
        "phone": "0501234567",
        "email": "anna@gmail.com",
        "city": "Rishon LeZion"
    },

    "Olga": {
        "phone": "0529876543",
        "email": "olga@gmail.com",
        "city": "Tel Aviv"
    },

    "Alex": {
        "phone": "0543456789",
        "email": "alex@gmail.com",
        "city": "Haifa"
    },

    "Kate": {
        "phone": "0534567890",
        "email": "kate@gmail.com",
        "city": "Ashdod"
    },

    "Max": {
        "phone": "0585678901",
        "email": "max@gmail.com",
        "city": "Holon"
    },

    "Maria": {
        "phone": "0506789012",
        "email": "maria@gmail.com",
        "city": "Bat Yam"
    },

    "David": {
        "phone": "0527890123",
        "email": "david@gmail.com",
        "city": "Bat Yam"
    },

    "Lola": {
        "phone": "0548901234",
        "email": "lola@gmail.com",
        "city": "Rishon LeZion"
    }
}

with open("book.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "phone", "email", "city"]
    )

    writer.writeheader()

    for name, info in my_phone_b.items():
        writer.writerow({
            "name": name,
            "phone": info["phone"],
            "email": info["email"],
            "city": info["city"]
        })


menu = [
    "1 - Show all contacts",
    "2 - Add friend",
    "3 - Change friend",
    "4 - Delete friend",
    "5 - Find friend",
    "6 - Find friend phone",
    "7 - Find friend city",
    "8 - Find friend email",
    
    "0 - Exit"
]


def show_all_contacts(book):
    for name,data in book.items():
        #print(f"Name in your book - {name} - {data}")
        print(f"""------------------------
        Name:  {name}
        Phone: {data['phone']}
        Email: {data['email']}
        City:  {data['city']}
       ------------------------""")
    
    #  print("------------------------")
    #         print(f"Name:  {name}")
    #         print(f"Phone: {data['phone']}")
    #         print(f"Email: {data['email']}")
    #         print(f"City:  {data['city']}")
    #     print("------------------------")
    
    

def add_friends(book):
    add_friend_key = input("Enter new name: ")
    add_new_phone = input("Enter new phone: ")
    add_new_email = input("Enter new email: ")
    add_new_city = input("Enter city: ")

    book[add_friend_key] = {
        "phone": add_new_phone,
        "email": add_new_email,
        "city": add_new_city
    }

    print(f"You added: {add_friend_key}\n===== UPDATED BOOK =====")
    show_all_contacts()
    


def change_friends(book):
    name_for_change = input("Enter name for change: ")

    if name_for_change in book:
        print(f"Friend found - {name_for_change}")

        choice_change = int(input(
            "What do you want to change? "
            "1 - phone | 2 - email | 3 - city: "
        ))

        if choice_change == 1:
            new_phone = input("Enter new phone: ")
            book[name_for_change]["phone"] = new_phone

        elif choice_change == 2:
            new_email = input("Enter new email: ")
            book[name_for_change]["email"] = new_email

        elif choice_change == 3:
            new_city = input("Enter new city: ")
            book[name_for_change]["city"] = new_city
            
    

        print("Contact updated!")

    else:
        print("Friend not found")
    
    
       
def delete_friends(book):
    del_name = input("Enter name for delete: ")

    if del_name in book:
        print(f"Friend found - {del_name}")
        book.pop(del_name)
        print(f"{del_name} - deleted")

    else:
        print("Friend not found")


def find_friend(book):
    name = input("Enter name: ")
    if name in book:
        print(book[name]["phone"])
        print(book[name]["email"])
        print(book[name]["city"])
    else:
        print("friend not found")
        

def find_friend_phone(book):
    phone = input("Enter phone: ")
    found = False

    for name, info in book.items():
        if info["phone"] == phone:
            print(f"""
------------------------
Name: {name}
Phone: {info["phone"]}
Email: {info["email"]}
City: {info["city"]}
------------------------
""")
            found = True

    if found == False:
        print("Friend not found")
    
def find_friend_city(book):
    city = input("Enter city: ")
    found = False

    for name, info in book.items():
        if info["city"] == city:
            print(f"""
------------------------
Name: {name}
Phone: {info["phone"]}
Email: {info["email"]}
City: {info["city"]}
------------------------
""")
            found = True

    if found == False:
        print("City not found")
           

def find_friend_email(book):
    email = input("Enter email: ")
    found = False

    for name, info in book.items():
        if info["email"] == email:
            print(f"""
------------------------
Name: {name}
Phone: {info["phone"]}
Email: {info["email"]}
City: {info["city"]}
------------------------
""")
            found = True

    if found == False:
        print("Emaila not found")
            
    
    
    
is_running = True
while is_running:

    for item in menu:
        print(item)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_all_contacts(my_phone_b)

    elif choice == 2:
        add_friends(my_phone_b)

    elif choice == 3:
        change_friends(my_phone_b)

    elif choice == 4:
        delete_friends(my_phone_b)
    
    elif choice == 5:
        find_friend(my_phone_b)
    
    elif choice == 6:
        find_friend_phone(my_phone_b)
        
    elif choice == 7:
        find_friend_city(my_phone_b)
        
    elif choice == 8:
        find_friend_email(my_phone_b)
        

    elif choice == 0:
        print("Exit!")
        is_running = False

