import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password =  'bismillah',
   
)

cursor = db.cursor()
print("Data berhasil disimpan")