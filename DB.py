import mysql

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="swen504cs"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM studentdb WHERE isDomesticStudent ='0'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
