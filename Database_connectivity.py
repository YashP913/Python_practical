import mysql.connector
Connect = mysql.connector.connect(host = "localhost",user = "root" , password = "root" , database = "world")
Cursor = Connect.cursor()
def Create():
  Cursor.execute("CREATE TABLE Student(Name varchar(50), Branch varchar(50) , city varchar(50))")
def Insert():
    sql = "INSERT INTO Student (Name, Branch , city) VALUES (%s, %s,%s)"
    val = ("Yash", "CSE","Tirora")
    Cursor.execute(sql, val)
    Connect.commit()
def Multiple_Insert():
    sql = "INSERT INTO Student (Name, Branch , city) VALUES (%s, %s,%s)"
    val = [("Mohit", "CSE","Tirora"),
           ("Sahil", "CSE","Bhandara"),
           ("Aman", "CSE","Nagpur"),
           ("Omsai", "CSE","Pandarkauda"),
           ("Pratyush", "CSE","Dharashiv"),]
    Cursor.executemany(sql, val)
    Connect.commit()
def Display():
   Cursor.execute("SELECT * FROM student") 
Multiple_Insert()      
Display()   