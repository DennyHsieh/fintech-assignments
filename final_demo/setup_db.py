import sqlite3
import csv

# Read data
with open('./final_demo_result.csv', newline='') as f:
    csv_reader = csv.DictReader(f)
    potential_result = [
        (row['profile_id'], row['name'], row['age'], row['title'], row['cnt'], row['keyword'])
        for row in csv_reader
    ]

# Create SQLite database
with open('create_db_potential.sql') as f:
    create_db_sql = f.read()

db = sqlite3.connect('final_demo_result.db')
with db:
    db.executescript(create_db_sql)
    db.executemany(
        'INSERT INTO potentialCrime (profile_id, name,age, title, cnt, keyword) VALUES (?, ?, ?, ?, ?, ?)',
        potential_result
    )
