import sqlite3

conn = sqlite3.connect("db/world_bank.db")
#Drop if exists
conn.execute("DROP TABLE IF EXISTS countries")
conn.execute("DROP TABLE IF EXISTS indicators")
conn.execute("DROP TABLE IF EXISTS datastore")
#creating tables
conn.execute('CREATE TABLE countries(id INTEGER PRIMARY KEY AUTOINCREMENT,country_name TEXT,iso_name TEXT)')
#creating tables
conn.execute(' CREATE TABLE indicators(id INTEGER PRIMARY KEY AUTOINCREMENT,indicatorname TEXT,code TEXT) ')

#creating tables
conn.execute(' CREATE TABLE datastore(id INTEGER PRIMARY KEY AUTOINCREMENT,countryid INTEGER,start_period INTEGER,end_period INTEGER,indicatorid)')
conn.close()