import sqlite3


conn = sqlite3.connect('custommers.db')

cur = conn.cursor()
cur.execute("CREATE TABLE customers first_name text,last_name text,email text,")

conn.commit()
conn.close()