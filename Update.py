import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(".env")

mysql_db = mysql.connector.connect(
    user="root",
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE")
)

my_cursor = mysql_db.cursor()

sql = "INSERT INTO employees (first_name, last_name, department, email) VALUES (%s, %s, %s, %s)"
val = ('Thomas', 'Mehl', 'WWL', 'fooo@mail.com')

my_cursor.execute(sql, val)
mysql_db.commit()

print(my_cursor.rowcount, "record inserted.")