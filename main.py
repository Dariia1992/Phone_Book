from functions import (
    show_all_contacts,
    add_friends,
    change_friends,
    delete_friends,
    find_friend,
    find_friend_phone,
    find_friend_city,
    find_friend_email
)
from storage import save_book





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

is_running = True

while is_running:

    for item in menu:
        print(item)

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_all_contacts(my_phone_b)

        elif choice == 2:
            add_friends(my_phone_b)
            save_book(my_phone_b)

        elif choice == 3:
            change_friends(my_phone_b)
            save_book(my_phone_b)

        elif choice == 4:
            delete_friends(my_phone_b)
            save_book(my_phone_b)

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

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a number!")
