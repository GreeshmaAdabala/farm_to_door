import sqlite3

conn = sqlite3.connect("farm.db")
cursor = conn.cursor()

# Farmers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS farmers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    password TEXT
)
""")

# Vegetable stock table
cursor.execute("""
CREATE TABLE IF NOT EXISTS vegetable_stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer_name TEXT,
    name TEXT,
    price REAL,
    quantity REAL
)
""")

# Customer details
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    alt_phone TEXT,
    email TEXT,
    address TEXT,
    order_type TEXT,
    payment_method TEXT
)
""")

# Customer orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    vegetable_name TEXT,
    quantity REAL,
    price_per_kg REAL,
    total_price REAL
)
""")

conn.commit()
conn.close()

print("✅ farm.db created and tables are ready.")
