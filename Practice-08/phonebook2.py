import psycopg2

conn = psycopg2.connect(
        dbname="phonebook_db",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
)

cursor = conn.cursor()


def search_contacts(pattern):
        cursor.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
        results = cursor.fetchall()
        return results

def upsert_contact(name, phone):
        cursor.execute("CALL upsert_contact(%s, %s);", (name, phone))
        conn.commit()
        print(f"Contact '{name}' inserted/updated successfully.")

def upsert_multiple_contacts(names, phones):
        cursor.execute(
            "SELECT * FROM upsert_multiple_contacts(%s, %s);",
            (names, phones)
        )
        invalid_entries = cursor.fetchall()
        return invalid_entries

def get_contacts_paginated(limit, offset):
        cursor.execute(
            "SELECT * FROM get_contacts_paginated(%s, %s);",
            (limit, offset)
        )
        results = cursor.fetchall()
        return results

def delete_contact(value):
        cursor.execute("CALL delete_contact(%s);", (value,))
        conn.commit()
        print(f"Deleted records matching: {value}")



print(search_contacts("Beka"))

upsert_contact("Beka",767)
print(search_contacts("Beka"))

names = ["Alice", "Bob", "Charlie"]
phones = ["555-1234", "abc", "+1 (555) 678-910"]
invalids = upsert_multiple_contacts(names, phones)
print("Invalid entries:", invalids)

page1 = get_contacts_paginated(5, 0)
print("Page 1:", page1)

delete_contact("Alice")
print(search_contacts("Alice"))

cursor.close()
conn.close()