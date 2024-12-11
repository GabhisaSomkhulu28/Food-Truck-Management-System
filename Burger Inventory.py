import sqlite3

def initialize_db():
    
    conn = sqlite3.connect('burger_inventory.db')
    cursor = conn.cursor()
        
    cursor.execute('CREATE TABLE IF NOT EXISTS  Ingredients(id INTEGER PRIMARY KEY, item_name TEXT, price INTEGER, quantity INTEGER)')

        
    cursor.execute('INSERT OR IGNORE INTO Ingredients (id, item_name, price, quantity) VALUES (?, ?, ?, ?)',
                    (101, 'Chicken Burger',60.00, 20))
    cursor.execute('INSERT OR IGNORE INTO Ingredients (id, item_name, price, quantity) VALUES (?, ?, ?, ?)',
                    (102, 'Beef Burger', 70.00, 20))
    cursor.execute('INSERT OR IGNORE INTO Ingredients (id, item_name, price, quantity) VALUES (?, ?, ?, ?)',
                    (103, 'Vegan Burger', 65.00, 15))
    cursor.execute('INSERT OR IGNORE INTO Ingredients (id, item_name, price, quantity) VALUES (?, ?, ?, ?)',
                    (104, 'Sweet Potato Chips', 30.00, 25))
    cursor.execute('INSERT OR IGNORE INTO Ingredients (id, item_name, price, quantity) VALUES (?, ?, ?, ?)',
                    (105, 'Regular Potato Chips',25.00, 30))
    cursor.execute('INSERT OR IGNORE INTO Ingredients (id, item_name, price, quantity) VALUES (?, ?, ?, ?)',
                    (106, 'Vanilla Ice Cream',7.00, 40))
    cursor.execute('INSERT OR IGNORE INTO Ingredients (id, item_name, price, quantity) VALUES (?, ?, ?, ?)',
                    (107, 'Chocolate Ice Cream',10.00, 40))
    cursor.execute('INSERT OR IGNORE INTO Ingredients (id, item_name, price, quantity) VALUES (?, ?, ?, ?)',
                    (108, 'Mix(Choco & Vanilla) Ice Cream', 12.00, 40))
    
    conn.commit()    

    print("Stock available :")
    cursor.execute('SELECT * FROM Ingredients')

    for row in cursor:
        print(row)

    conn.commit
    cursor.close()

initialize_db()

