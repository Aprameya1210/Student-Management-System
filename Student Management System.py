import mysql.connector

m = str()
print(("STUDENT REGISTRATION SYSTEM".ljust(60)).rjust(90))


def main():
    global m
    database_name = str(input("Enter Database Name : "))
    database_password = str(input("Enter Password to your database : "))
    try:
        m = mysql.connector.connect(host="localhost", user="root", passwd=database_password, database=database_name)
        print("WELCOME !!")
        options()
    except mysql.connector.errors.ProgrammingError:
        print("Wrong database or password given.")
        print("ACCESS DENIED.")
    

def new_user():
    global m
    a = m.cursor()
    a.execute("create table student(Enroll_No int(5) not null auto_increment,Name varchar(30),DOB date,email varchar(100),phone_no varchar(50),primary key(Enroll_No))")
    print("TABLE CREATED.")
    m.commit()
    a.close()


def options():
    print("CHOOSE AN APPROPRIATE OPTION FOR YOUR USE : ")
    print("1. Add the info of a new student.")
    print("2. Retrieve info of a new student.")
    print("3. Update info of an existing student.")
    print("4. Delete the details of a student")
    print("5. Display all records.")
    print("6. Exit the software.")
    print("CHOOSE YOUR OPTION : ")
    a = input()
    if a == '1':
        add_new_student()
    if a == '2':
        view_info()
    if a == '3':
        update_student()
    if a == '4':
        delete_existing_record()
    if a == '5':
        show_table()
    if a == '6':
        exiting_software()


def add_new_student():
    global m
    name = str(input("Enter the name of the new student : "))
    dob = str(input("Enter DOB of the new student (YYYY-MM-DD) : "))
    email = str(input("Enter the mail address of the new student : "))
    phone_no = str(input("Enter the phone number of the new student : "))
    a = m.cursor()
    a.execute("INSERT INTO student(Name,DOB,email,phone_no)"+"VALUES('"+name.upper()+"','"+dob+"','"+email+"','"+phone_no+"')")
    a.execute("select max(Enroll_No) from student")
    records = a.fetchall()
    m.commit()
    a.close()
    print("Record Added.")
    print("Your Enrollment no. is : "+str(records)[2:-3])
    options()


def view_info():
    global m
    print("1-Search by Name")
    print("2-Search by DOB")
    print("3-Search by email")
    print("4-Search by Phone No.")
    print("5-Search by Enrollment No.")
    b = int(input("Enter your choice : "))
    if b == 1:
        print("Enter the name you want to search")
        n = str(input())
        a = m.cursor()
        a.execute("select*from student where Name='"+n.upper()+"'")
        records = a.fetchall()
        if records != []:
            print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
            for record in records:
                print(str(record[0]).ljust(5)+" | "+str(record[1]).ljust(30)+" | "+str(record[2]).ljust(10)+" | "+str(record[3]).ljust(50)+" | "+str(record[4]).ljust(12))
        else:
            print("Record not found.")
        m.commit()
        a.close()
    elif b == 2:
        print("Enter the DOB you want to search(YYYY-MM-DD) : ")
        n1 = str(input())
        a = m.cursor()
        a.execute("select*from student where DOB='"+n1+"'")
        records = a.fetchall()
        if records != []:
            print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
            for record in records:
                print(str(record[0]).ljust(5)+" | "+str(record[1]).ljust(30)+" | "+str(record[2]).ljust(10)+" | "+str(record[3]).ljust(50)+" | "+str(record[4]).ljust(12))
        else:
            print("Record not found.")
        m.commit()
        a.close()
    elif b == 3:
        print(("Enter the E-Mail you want to search : "))
        n2 = str(input())
        a = m.cursor()
        a.execute("select*from student where email='"+n2+"'")
        records = a.fetchall()
        if records != []:
            print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
            for record in records:
                print(str(record[0]).ljust(5)+" | "+str(record[1]).ljust(30)+" | "+str(record[2]).ljust(10)+" | "+str(record[3]).ljust(50)+" | "+str(record[4]).ljust(12))
        else:
            print("Record not found.")
            m.commit()
            a.close()
    elif b == 4:
        print("Enter the phone no. you want to search : ")
        n3 = input()
        a = m.cursor()
        a.execute("select*from student where phone_no='"+str(n3)+"'")
        records = a.fetchall()
        if records != []:
            print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
            for record in records:
                print(str(record[0]).ljust(5)+" | "+str(record[1]).ljust(30)+" | "+str(record[2]).ljust(10)+" | "+str(record[3]).ljust(50)+" | "+str(record[4]).ljust(12))
        else:
            print("Record not found.")
            m.commit()
            a.close()
    elif b == 5:
        print("Enter the Enrollment No. you want to search : ")
        n4 = input()
        a = m.cursor()
        a.execute("select*from student where Enroll_No="+str(n4))
        records = a.fetchall()
        if records != []:
            print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
            for i in records:
                print(str(i[0]).ljust(5)+" | "+str(i[1]).ljust(30)+" | "+str(i[2]).ljust(10)+" | "+str(i[3]).ljust(50)+" | "+str(i[4]).ljust(12))
        else:
            print("Record not found.")
            m.commit()
            a.close()
    options()



def update_name():
    global m
    x = int(input("Enter Enrollment No. : "))
    print("Enter new name : ")
    new_detail = str(input())
    conf = input("Are you sure you want to update ? (y/n) : ")
    if conf == "y" or conf == "Y":
        a = m.cursor()
        a.execute("update student"+"\n"+"set Name='"+new_detail.upper()+"'\n"+"where Enroll_No="+str(x))
        a.execute("select*from student where Enroll_No=('"+str(x)+"')")
        records = a.fetchall()
        print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
        for i in records:
            print(str(i[0]).ljust(5)+" | "+str(i[1]).ljust(30)+" | "+str(i[2]).ljust(10)+" | "+str(i[3]).ljust(50)+" | "+str(i[4]).ljust(12))
        m.commit()
        a.close()
        print("Record changed.")
        options()
    else:
        options()


def update_mail_address():
    global m
    x = int(input("Enter Enrollment No. : "))
    print("Enter new E-mail : ")
    new_detail = str(input())
    conf = input("Are you sure you want to update ? (y/n) : ")
    if conf == "y" or conf == "Y":
        a = m.cursor()
        a.execute("update student"+"\n"+"set email='"+new_detail+"'\n"+"where Enroll_No="+str(x))
        a.execute("select*from student where Enroll_No=('"+str(x)+"')")
        records = a.fetchall()
        print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
        for i in records:
            print(str(i[0]).ljust(5)+" | "+str(i[1]).ljust(30)+" | "+str(i[2]).ljust(10)+" | "+str(i[3]).ljust(50)+" | "+str(i[4]).ljust(12))
        m.commit()
        a.close()
        print("Record changed.")
        options()
    else:
        options()


def update_phone_no():
    global m
    x = int(input("Enter Enrollment No. : "))
    print("Enter new Phone No. : ")
    new_detail = str(input())
    conf = input("Are you sure you want to update ? (y/n) : ")
    if conf == "y" or conf == "Y":
        a = m.cursor()
        a.execute("update student"+"\n"+"set phone_no='"+new_detail+"'\n"+"where Enroll_No="+str(x))
        a.execute("select*from student where Enroll_No=('"+str(x)+"')")
        records = a.fetchall()
        print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
        for i in records:
            print(str(i[0]).ljust(5)+" | "+str(i[1]).ljust(30)+" | "+str(i[2]).ljust(10)+" | "+str(i[3]).ljust(50)+" | "+str(i[4]).ljust(12))
        m.commit()
        a.close()
        print("Record changed.")
        options()
    else:
        options()


def update_dob():
    global m
    x = int(input("Enter Enrollment No. : "))
    print("Enter new DOB (YYYY-MM-DD) : ")
    new_detail = input()
    conf = input("Are you sure you want to update ? (y/n) : ")
    if conf == "y" or conf == "Y":
        a = m.cursor()
        a.execute("update student set DOB='"+new_detail+"' where Enroll_No="+str(x))
        a.execute("select*from student where Enroll_No=('"+str(x)+"')")
        records = a.fetchall()
        print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
        for i in records:
            print(str(i[0]).ljust(5)+" | "+str(i[1]).ljust(30)+" | "+str(i[2]).ljust(10)+" | "+str(i[3]).ljust(50)+" | "+str(i[4]).ljust(12))
        m.commit()
        a.close()
        print("Record changed.")
        options()
    else:
        options()


def update_student():
    print("What info would you like to update ?")
    print("1. Update Student Name")
    print("2. Update mail address of the student")
    print("3. Update phone no. of the student")
    print("4. Update DOB of the student")
    x = int(input("Enter your choice : "))
    if x == 1:
        update_name()
        options()
    elif x == 2:
        update_mail_address()
        options()
    elif x == 3:
        update_phone_no()
        options()
    elif x == 4:
        update_dob()
        options()


def delete_existing_record():
    global m
    print("Enter the enrollment no. of the student whose details you want to delete : ")
    enroll_no = str(input())
    a = m.cursor()
    a.execute("select*from student where Enroll_No="+enroll_no)
    records = a.fetchall()
    if records != []:
        for i in records:
            print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
            print(str(i[0]).ljust(5)+" | "+str(i[1]).ljust(30)+" | "+str(i[2]).ljust(10)+" | "+str(i[3]).ljust(50)+" | "+str(i[4]).ljust(12))
            conf = input("Are you sure you want to delete this record ? (y/n) : ")
            if conf == "y" or conf == "Y":
                a.execute("delete from student where Enroll_No="+enroll_no)
                m.commit()
                a.close()
                print("Record Deletion Confirmed.")
                options()
            else:
                options()
    elif records == []:
        print("Wrong Input.")
        print("No student with this enrollment no.")
        print("Try Again.")
        delete_existing_record()
        options()


def exiting_software():
    x = str(input("Are you sure you want to exit the software ? (y/n) : "))
    if x == "y" or x == "Y":
        print("Thank you for using the software.")
        quit()
    else:
        print("Choose another option.")
        options()


def show_table():
    global m
    a = m.cursor()
    a.execute("select*from student")
    records = a.fetchall()
    print("E.No.".ljust(5)+" | "+"Name".ljust(30)+" | "+"DOB".ljust(10)+" | "+"E-Mail".ljust(50)+" | "+"Phone No.".ljust(12))
    for i in records:
        print(str(i[0]).ljust(5)+" | "+str(i[1]).ljust(30)+" | "+str(i[2]).ljust(10)+" | "+str(i[3]).ljust(50)+" | "+str(i[4]).ljust(12))
    m.commit()
    a.close()
    options()

def password():
    password_entry = input("Enter the password : ")
    if password_entry == "kj316ap489z":
        main()
        x = str(input("Are you using this on your PC for the first time (Y/N) : "))
        if x == "y" or x == "Y":
            new_user()
            options()
        elif x == "n" or x == "N":
            options()
    else:
        print("Wrong Password.")
        password()
main()

