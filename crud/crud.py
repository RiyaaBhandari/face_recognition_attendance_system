import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="testdataset")
mysqlcursor=mysqldb.cursor()
#to create the table
#mysqlcursor.execute("create table studentrecord(rollno INT,name VARCHAR(30),marks INT)")
#insert into table
'''
try:
   mysqlcursor.execute("insert into studentrecord(rollno,name,marks) values(2,'siya',98)")
   mysqldb.commit()
   print("record inserted into the table")
except:
   mysqldb.rollback()

mysqldb.close()
'''

#display operation
'''
try:
    mysqlcursor.execute("select * from studentrecord")
    result=mysqlcursor.fetchall()
    for i in result:
        roll=i[0]
        name=i[1]
        marks=i[2]
        print(roll,name,marks)
except:
    print("some issue in the code")

mysqlcursor.close()

'''

#update the record
'''
try:
    mysqlcursor.execute("update studentrecord set name='golu' where rollno=1")
    mysqldb.commit()
except:
    mysqldb.rollback()

'''

# delete operation
try:
    mysqlcursor.execute("delete from studentrecord where rollno=1")
    mysqldb.commit()
    print("deletion success")
except:
    mysqldb.rollback()
