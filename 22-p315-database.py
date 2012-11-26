import sqlite3
connection  = sqlite3.connect('test.sqlite')
cursor = connection.cursor()
cursor.execute("""SELECT DATE('NOW')""")
connection.commit()
connection.close()
