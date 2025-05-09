import sqlite3

try: 
    with sqlite3.connect('../db/magazines.db') as conn:
        print("DB connected")

        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # publishers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL UNIQUE
            )
        """)

        # magazines table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
            )
        """)

         # subscribers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL UNIQUE,
                address TEXT NOT NULL
            )
        """)

        # subscribers table (join table)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY, 
                subscriber_id INTEGER NOT NULL, 
                magazine_id  INTEGER NOT NULL, 
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
            )
        """)

        print("Tables created successfully.")

        def add_publisher(cursor, name):
            try: 
                cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
            except sqlite3.IntegrityError:
                print(f"Publisher '{name}' already exist")

        def add_magazine(cursor, name, publisher_name):
            cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
            result = cursor.fetchone()
            if result:
                publisher_id = result[0]
                try: 
                    cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
                except sqlite3.IntegrityError:
                    print(f"Magazine '{name}' already exist")
            else:
                print(f"Publisher '{publisher_name}' not found.")

        def add_subscriber(cursor, name, address):
            cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
            if cursor.fetchone():
                print(f"Subscriber '{name}' at '{address}' already exists.")
                return
            try:
                cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
            except sqlite3.IntegrityError:
                print(f"Error adding subscriber '{name}'.")

        def add_subscription(cursor, subscriber_name, magazine_name, expiration_date):
            cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
            sub = cursor.fetchone()
            cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
            mag = cursor.fetchone()
            if sub and mag:
                subscriber_id = sub[0]
                magazine_id = mag[0]
                cursor.execute("""
                    SELECT * FROM subscriptions 
                    WHERE subscriber_id = ? AND magazine_id = ?
                """, (subscriber_id, magazine_id))
                if cursor.fetchone():
                    print(f"Subscription already exists for {subscriber_name} to {magazine_name}.")
                    return
                try:
                    cursor.execute("""INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)""", (subscriber_id, magazine_id, expiration_date))
                except sqlite3.IntegrityError:
                    print(f"Error adding subscription.")
            else:
                print(f"Subscriber or magazine not found for subscription.")
        

        add_publisher(cursor, "Publisher 1")
        add_publisher(cursor, "Publisher 2")
        add_publisher(cursor, "Publisher 3")

        add_magazine(cursor, "Magazine 1", "Publisher 1")
        add_magazine(cursor, "Magazine 2", "Publisher 2")
        add_magazine(cursor, "Magazine 3", "Publisher 3")

        add_subscriber(cursor, "Anna Doe", "123 Maple Street")
        add_subscriber(cursor, "Sam Doe", "456 Oak Avenue")
        add_subscriber(cursor, "Kate Doe", "789 Pine Road")

        add_subscription(cursor, "Anna Doe", "Magazine 1", "2025-01-01")
        add_subscription(cursor, "Sam Doe", "Magazine 2", "2025-01-02")
        add_subscription(cursor, "Kate Doe", "Magazine 3", "2025-01-03")
        
        conn.commit()
        print("Sample data inserted successfully.")

        print("All Subscribers:")
        try:
            cursor.execute("SELECT * FROM subscribers")
            for row in cursor.fetchall():
                print(row)
        except sqlite3.Error as e:
            print("Error retrieving subscribers:", e)

        print("All Magazines Sorted by Name:")
        try:
            cursor.execute("SELECT * FROM magazines ORDER BY name")
            for row in cursor.fetchall():
                print(row)
        except sqlite3.Error as e:
            print("Error retrieving magazines:", e)

        print("Magazines Published by 'Publisher 1':")
        try:
            cursor.execute("""
                SELECT m.name 
                FROM magazines m
                JOIN publishers p ON m.publisher_id = p.publisher_id
                WHERE p.name = 'Publisher 1'
            """)
            for row in cursor.fetchall():
                print(row)
        except sqlite3.Error as e:
            print("Error retrieving magazines by publisher:", e)
        
except sqlite3.Error as e:
    print(f"An error: {e}")