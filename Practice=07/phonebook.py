import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# INSERT FROM CSV

def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, phone = row
            try:
                cur.execute(
                    "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
                    (name, phone)
                )
            except Exception as e:
                print(f"Error inserting {row}: {e}")
                conn.rollback()
        conn.commit()
    print("CSV data inserted successfully.")

# INSERT FROM CONSOLE

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    try:
        cur.execute(
            "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact added!")
    except Exception as e:
        print("Error:", e)
        conn.rollback()

# UPDATE CONTACT

def update_contact():
    name = input("Enter existing name: ")
    new_name = input("Enter new name (or press Enter to skip): ")
    new_phone = input("Enter new phone (or press Enter to skip): ")

    if new_name:
        cur.execute(
            "UPDATE contacts SET first_name=%s WHERE first_name=%s",
            (new_name, name)
        )

    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone=%s WHERE first_name=%s",
            (new_phone, name)
        )

    conn.commit()
    print("Contact updated.")

# QUERY CONTACTS

def query_contacts():
    print("1. Search by name")
    print("2. Search by phone prefix")
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM contacts WHERE first_name ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == "2":
        prefix = input("Enter phone prefix: ")
        cur.execute(
            "SELECT * FROM contacts WHERE phone LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

# DELETE CONTACT

def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "DELETE FROM contacts WHERE first_name=%s",
            (name,)
        )

    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute(
            "DELETE FROM contacts WHERE phone=%s",
            (phone,)
        )

    conn.commit()
    print("Contact deleted.")


# MENU

def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            path = input("Enter CSV file path: ")
            insert_from_csv(path)

        elif choice == "2":
            insert_from_console()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            query_contacts()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            break

        else:
            print("Invalid option!")

menu()

cur.close()
conn.close()