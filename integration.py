import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
mycursor=mydb.cursor()
print("This is a Neighbourhood Crime Management System (NCMS) which aims to provide a centralised,and organised dataset of the low-level crimes, taking place in out proximity")
def adddata():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    llist=[]
    a=int(input("Enter Id number: "))
    llist.append(a)
    b=input("Enter Offender Name: ")
    llist.append(b)
    c=int(input("Enter Age of Offender: "))
    llist.append(c)
    d=input("Enter Crime committed by offender: ")     
    llist.append(d)
    e=input("Enter date of crime committed: ")
    llist.append(e)
    f=input("Enter date of record entry: ")
    llist.append(f)
    g=int (input ("Enter number of witnesses: "))
    llist.append(g)
    print(llist)
    rec=(llist)
    sql="insert into criminals(id,Name,Age,crime_commited,date_of_crime,date_of_record,eyewitness)values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,rec)
    print("Record Added")
    mydb.commit()
        

def deldata():
    import mysql.connector
    Mydb = mysql.connector.connect (host="localhost", user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender you want to delete")
    a1=input("Enter the ID Number")
    info=(a1,)
    sql=("delete from criminals where id=%s")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Record Deleted")

def fetchdata():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender you want to view")
    b1=input("Enter the ID Number")
    data=(b1,)
    sql=("select * from criminals where id=%s")
    mycursor.execute(sql,data)
    myrecords= mycursor.fetchall()
    for x in myrecords:
        print(x)
    

def sortdata():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    choice4=0
    choice4=input("Select the order for the records to be sorted: \n 1.Ascending\n 2.Descending \n")
    if choice4=="1":
        sql=("select id,Name,Age,crime_commited,date_of_crime,date_of_record,eyewitness from criminals order by Age ASC")
        mycursor.execute(sql)
        myrecords= mycursor.fetchall()
        for x in myrecords:
            print(x)
        mydb.commit()
    elif choice4=="2":
        sql2=("select id,Name,Age,crime_commited,date_of_crime,date_of_record,eyewitness from criminals order by Age DESC")
        mycursor.execute(sql2)
        myrecords= mycursor.fetchall()
        for x in myrecords:
            print(x)
        mydb.commit()
    else:
       print("Wrong input")
            

def updname():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Name:")
    info=(c2,c1)
    sql=("update criminals set Name= %s where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")

def updage():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Age:")
    info=(c2,c1)
    sql=("update criminals set Age= %s  where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")

def updcrime():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Crime:")
    info=(c2,c1)
    sql=("update criminals set crime= %s where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")
        
def upddateofc():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Date of crime:")
    info=(c2,c1)
    sql=("update criminals set date_of_crime=%s where id=%s")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")

def updentry():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter Date of entry:")
    info=(c2,c1)
    sql=("update criminals set date_of_record='%s' where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")

def updwitness():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Number Of Witnesses:")
    info=(c2,c1)
    sql=("update criminals set eyewitness= %s  where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")

while True:
    print("CRIME MANAGEMENT SYSTEM: MENU")
    print("1. Add a new record")
    print("2. Edit an existing record")
    print("3. View records")
    print("4. Delete record")
    print("5. Sort on the basis of age of offender")
    print("6. Exit")
    choice= int(input("What's your choice?(1-6)\nAnswer: "))
    if choice==1:
        adddata()
    elif choice==2:
        updatedata()
    elif choice==3:
        fetchdata()
    elif choice==4:
        deldata()
    elif choice==5:
        sortdata()
    elif choice==6:
        print("Exiting")
        break
