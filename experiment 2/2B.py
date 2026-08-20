import pandas as pd
import sqlite3
import os
# Remove old database
if os.path.exists("students.db"):
    os.remove("students.db")
# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
# Create table
cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")
# Insert records
cursor.execute("INSERT INTO students VALUES (1, 'John')")
cursor.execute("INSERT INTO students VALUES (2, 'Jane')")
conn.commit()
# Query the database
df = pd.read_sql_query("SELECT * FROM students", conn)
print("Students Data:")
print(df)
# Update record
cursor.execute("UPDATE students SET name='Alice' WHERE id=1")
# Delete record
cursor.execute("DELETE FROM students WHERE id=1")
conn.commit()
conn.close()