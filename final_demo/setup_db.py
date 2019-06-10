import sqlite3
import csv

# Read data
with open('./final_demo_result.csv', newline='') as f:
    csv_reader = csv.DictReader(f)
    potential_result = [(row['name'], row['age'], row['title'], row['crime'], row['crime_risk'],
                         row['key_sentence'], row['news_title'], row['news_link'], row['other_suspect'],
                         row['suspect_probability']) for row in csv_reader]

# Create SQLite database
with open('create_db_potential.sql') as f:
    create_db_sql = f.read()

db = sqlite3.connect('final_demo_result.db')
with db:
    db.executescript(create_db_sql)
    db.executemany(
        'INSERT INTO potentialCrime (name, age, title, keyword, crime_risk, cnt, news_title, news_link, other_suspect, suspect_probability) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        potential_result)
