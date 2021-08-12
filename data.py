import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="dental"
)

mycursor = mydb.cursor()

sql = "INSERT INTO dentaluser (UID, Uprss, Fname, Lname, DEMail) VALUES (%s, %s, %s, %s, %s)"
val = ("birdking123", "bird1234", "bird", "king", "birdking@gmail.com")
mycursor.execute(sql, val)
 
mydb.commit()

print(mycursor.rowcount, "record inserted.")