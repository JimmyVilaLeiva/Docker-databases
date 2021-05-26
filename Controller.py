import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(".env")
mydb = mysql.connector.connect(
    user="root",
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE")
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)