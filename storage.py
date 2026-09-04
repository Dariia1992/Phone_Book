import csv


def save_book(book):
    with open("book.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f,delimiter="|",fieldnames=["name", "phone", "email", "city"]
        )

        writer.writeheader()

        for name, info in book.items():
            writer.writerow({
                "name": name,
                "phone": info["phone"],
                "email": info["email"],
                "city": info["city"]
            })