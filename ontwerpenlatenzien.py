import sqlite3

conn = sqlite3.connect('printer_data.db')
cursor = conn.cursor()

cursor.execute('''
SELECT * FROM prints
''')

fulldata = [row for row in cursor.fetchall()]
names = [el[1] for el in fulldata]

conn.close()
print( names)
print(fulldata)
