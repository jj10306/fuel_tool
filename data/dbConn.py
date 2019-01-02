from vehicles import skinny_list
import sqlite3


con = sqlite3.connect('vehicles.db')
cursor = con.cursor()
# cursor.execute("SELECT * FROM vehicle")
# print(cursor.fetchall())
try:
    cursor.execute("CREATE TABLE vehicle (id, make, model, year, fuel_type, mpg)")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
except:
    pass
for aDict in skinny_list:
    cursor.execute("""INSERT INTO vehicle
                        VALUES (?, ?, ?, ?, ?, ?)""",
                         (aDict["id"], aDict['make'], aDict['model'], aDict['year'], aDict['fuelType'], aDict['comb08']))


cursor.execute("SELECT * FROM vehicle")
print("Query Results:")
print(cursor.fetchone())

con.commit()
con.close()






