import sqlite3

conn = sqlite3.connect("issues.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS issues(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
title TEXT,
category TEXT,
description TEXT,
location TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
