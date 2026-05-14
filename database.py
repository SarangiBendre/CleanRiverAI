import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# HISTORY TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    river TEXT,
    location TEXT,
    count INTEGER,
    level TEXT,
    image TEXT,
    output TEXT,
    date TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()

print("Database Ready ✅")