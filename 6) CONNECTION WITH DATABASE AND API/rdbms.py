import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Aruna@123',
    database='college2')
mycursor = conn.cursor()
mycursor.execute('create table student2(Roll_no numeric(4) primary key,Age numeric (3),Marks_percentage decimal(4,2),Attendance_percentage decimal(4,2))')
mycursor.execute('insert into student2 VALUES (1, 19,98,97)')
conn.commit()
print(mycursor.rowcount, "record(s) inserted")
mycursor.execute('insert into student2 VALUES (2, 20,91,78)')
conn.commit()
print(mycursor.rowcount, "record(s) inserted")

mycursor.execute('insert into student2 VALUES (12, 19,68,67),(3,20,67,54),(4,18,86,78),(5,17,98,75),(6,21,65,87),(7,20,98,74),(8,22,69,45),(9,32,74,55)')
conn.commit()
print(mycursor.rowcount, "record(s) inserted")

mycursor.execute('update  student2 set Attendance_percentage=90 where Marks_percentage>=90')
conn.commit()
print(mycursor.rowcount, "record(s) updated")

mycursor.execute('alter table student2 add column Status varchar(10)')
conn.commit()
print("colummn added")

mycursor.execute('update student2 set Status="Detained" where Attendance_percentage<85')
conn.commit()
print(mycursor.rowcount, "record(s) updated")

mycursor.execute('delete from student2 where Roll_no=12')
conn.commit()
print(mycursor.rowcount, "record(s) deleted")

mycursor.execute('delete from student2 where Attendance_percentage <=65')
conn.commit()
print(mycursor.rowcount, "record(s) deleted")

mycursor.execute("SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'student2' AND table_schema = 'college2'")
result = mycursor.fetchone()  # Retrieve the result
column_count = result[0]  # Access the count
print(column_count)

mycursor.execute('show tables')
tables = mycursor.fetchall()
for table in tables:
    print(table[0])
conn.commit()
mycursor.close()