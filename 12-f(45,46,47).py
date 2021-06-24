import mysql.connector as roll_number_fortyfive_fortysix_fortyseven
v=input(" Enter Your Mysql Password : ")
ashish_sir=roll_number_fortyfive_fortysix_fortyseven.connect(host="localhost", user = "root", passwd=v)

if ashish_sir.is_connected():
    print("Successfully Connected to MySQL")
else:
    print("connection failed!")
    
cursor=ashish_sir.cursor()
cursor.execute("create database if not exists LIBRARY_MANAGEMENT ")
ashish_sir.commit()

import mysql.connector as twelft_f
vaibhav = twelft_f.connect(host="localhost", user = "root", passwd="vaibhav",database="LIBRARY_MANAGEMENT")

if vaibhav.is_connected():
    print("Successfully Connected to LIBRARY_MANAGEMENT database")
else:
    print("connection failed!")

cursor=vaibhav.cursor()
cursor.execute("drop table if exists add_book,issue_book,register_for_membership,return_book")
cursor.execute("create table add_book(book_code varchar(50) not null unique,name_of_book varchar(50),author_name varchar(50),publication_name varchar(50),rack_number varchar(50)) ")
cursor.execute("insert into add_book values ( '100001','Computer Science','Sumita Arora','Dhanpat Rai & Corporation','1/C1') ")
cursor.execute("insert into add_book values ( '100002','Dime','Malva J. Lewis','Macmillan','1/C2') ")
cursor.execute("insert into add_book values ( '100003','Art,Craft,Design','Maureen Roche','Gill & Macmillan ','1/b1') ")
cursor.execute("insert into add_book values ( '100004','Comprehensive English Course','U. Narinesingh','Royards','2/a1') ")
cursor.execute("insert into add_book values ( '100005','Introducing Geography : Caribbean Focus','Sullivan-Sirjue','Carlong','2/b2') ")
cursor.execute("insert into add_book values ( '100006','Carlong Secondary Social Studies','W. Browne','Carlong','3/c1') ")
cursor.execute("insert into add_book values ( '100007','Creating a Nation : Jamica','G. Robinson','Carlong','1/a1') ")
cursor.execute("insert into add_book values ( '100008','Interact with Information Technology','Michele Taylor','Pearson Education','3/C2') ")
cursor.execute("insert into add_book values ( '100009','A Complete Mathematics Course','Raymond Toolsie','Caribbean Education Publishers','1/C2') ")
cursor.execute("insert into add_book values ( '100010','Health Family Life Education','Gerard Drakes','Macmillan','2/C1') ")
cursor.execute("insert into add_book values ( '100011','Integrated Science For Jamaica','W. Braithwaite','Macmillan','1/b1') ")
cursor.execute("create table issue_book(name varchar(50),registration_number varchar(50),book_code varchar(50),name_of_book varchar(50),issue_date varchar(50))")
cursor.execute("create table register_for_membership(name varchar(50),gender varchar(50),dob varchar(50),contact_number varchar(50),email_id varchar(50),occupation varchar(50),address varchar(100),membership_plan varchar(30))")
cursor.execute("insert into register_for_membership values ( 'Vaibhav Farenjiya','Male','30/10/2002','9617972927','vfk@gmail.com','Student','bhilai','3-month plan') ")
cursor.execute("insert into register_for_membership values ( 'Sugam','Male','20/1/2001','3454972927','sugam@gmail.com','Student','bhilai','2-month plan') ")
cursor.execute("insert into register_for_membership values ( 'Sudeep','Male','3/7/2003','9776869237','sudeep@gmail.com','Student','bhilai','1-month plan') ")
cursor.execute("create table return_book(book_code varchar(50),registration_number varchar(50),dor varchar(50),name_of_book varchar(50),author_name varchar(50),publication_name varchar(50),rack_number varchar(50))")
vaibhav.commit()

def add_book(a,b,c,d,m):
    Data_Insertion="insert into add_book(book_code,name_of_book,author_name,publication_name,rack_number) values( '{}','{}','{}','{}','{}' )".format(a,b,c,d,m)
    cursor=vaibhav.cursor()
    cursor.execute(Data_Insertion)
    vaibhav.commit()
    print("BOOK ADDED SUCCESSFULLY")
    main()

def book_list():
    cursor=vaibhav.cursor()
    cursor.execute("select * from add_book")
    data=cursor.fetchall()
    count=cursor.rowcount
    print("Total number of Books available",count)
    for row in data:
        print(row)
    main()

def return_book(book_code,registration_number,dor,name_of_book,author_name,publication_name,rack_number):
    book="insert into return_book(book_code,registration_number,dor,name_of_book,author_name,publication_name,rack_number) values( '{}','{}','{}','{}','{}','{}','{}')".format(book_code,registration_number,dor,name_of_book,author_name,publication_name,rack_number)
    cursor=vaibhav.cursor()
    cursor.execute(book)
    vaibhav.commit()
    
    add="insert into add_book(book_code,name_of_book,author_name,publication_name,rack_number) values( '{}','{}','{}','{}','{}' )".format(book_code,name_of_book,author_name,publication_name,rack_number)
    cursor=vaibhav.cursor()
    cursor.execute(add)
    vaibhav.commit()
    
    cursor=vaibhav.cursor()
    cursor.execute("delete from issue_book where book_code=book_code")
    vaibhav.commit()
    print( "Book Returned")
    main()
    
def issue_book(book_code,name_of_book,issue_date):
    name=input("Enter Student Name : ")
    registration_number=input("Enter Registration Id : ")
    a="insert into issue_book(name,registration_number,book_code,name_of_book,issue_date) values( '{}','{}','{}','{}','{}' )".format(name,registration_number,book_code,name_of_book,issue_date)
    cursor=vaibhav.cursor()
    cursor.execute(a)
    vaibhav.commit()
    cursor=vaibhav.cursor()
    cursor.execute("delete from add_book where book_code=book_code")
    vaibhav.commit()
    print( "Book Issued")
    main()
           
def register_for_membership(e,f,g,h,i,j,k,l):
    Data_Insertion="insert into register_for_membership(name,gender,dob,contact_number,email_id,occupation,address,membership_plan) values( '{}','{}','{}',{},'{}','{}','{}','{}' )".format(e,f,g,h,i,j,k,l)
    cursor=vaibhav.cursor()
    cursor.execute(Data_Insertion)
    vaibhav.commit()
    print("REGISTERED SUCCESSFULLY")
    main()

def issued_books_rocord():
    cursor=vaibhav.cursor()
    cursor.execute("select * from issue_book")
    data=cursor.fetchall()
    count=cursor.rowcount
    print("Total number of Books issued",count)
    for row in data:
        print(row)
    main()

def returned_book_record():
    cursor=vaibhav.cursor()
    cursor.execute("select * from return_book")
    data=cursor.fetchall()
    count=cursor.rowcount
    print("Total number of Books returned",count)
    for row in data:
        print(row)
    main()

def membership_record():
    cursor=vaibhav.cursor()
    cursor.execute("select * from register_for_membership")
    data=cursor.fetchall()
    count=cursor.rowcount
    print("Total of students who have membership",count)
    for row in data:
        print(row)
    main()
    

def main():
    print("""
====================== WELCOME TO SENIOR SECONDARY SECTOR-X LIBRARY ======================

    1.REGISTER FOR MEMBERSHIP
    *Members need to visit the library for Registeration ID within 5 days.
    
    2.VIEW BOOK LIST
    
    3.ISSUE BOOK TO STUDENT
    *We recommend to view booklist first to find the book physically and issue it easily.
    
    4.RETURN BOOK
    
    5.ADD BOOK DETAILS
    
    6.RECORD OF ISSUED BOOKS
    
    7.RECORD OF RETURNED BOOKS
    
    8.MEMBERSHIP RECORD
     
      """)
    
    choice=int(input("Enter choice : "))

    if choice == 1:
        name=input(str("Enter Name : "))
        gender=input(str("Enter Gender : "))
        dob=input("Enter Date Of Birth : ")
        contact_number=input("Enter Contact No. : ")
        email_id=input("Enter Email : ")
        occupation=input(str("Enter Occupation : "))
        address=input("Enter Address : ")
        membership_plan=input("Enter Membership Plan: ")
        member=register_for_membership(name,gender,dob,contact_number,email_id,occupation,address,membership_plan)

    elif choice == 2:
        book_list()

    elif choice == 3:
        book_code=input("Enter Book Code : ")
        name_of_book=input("Enter Book Name : ")
        issue_date=input("Enter Issue Date : ")
        issue=issue_book(book_code,name_of_book,issue_date)


    elif choice == 4:
        book_code=input("Enter Book Code : ")
        registration_number=input("registration id : ")
        dor=input("Enter Date Of Return : ")
        name_of_book=input("Enter Book Name : ")
        author_name=input("Enter Author Name : ")
        publication_name=input("Enter Publication Name : ")
        rack_number=input("Rack Number : ")
        returned=return_book(book_code,registration_number,dor,name_of_book,author_name,publication_name,rack_number)

    elif choice == 5:
        book_code=input("Enter Book Code : ")
        name_of_book=input("Enter Book Name : ")
        author_name=input("Enter Author Name : ")
        publication_name=input("Enter Publication Name : ")
        rack_number=input("Rack Number : ")
        add= add_book(book_code,name_of_book,author_name,publication_name,rack_number)

    elif choice == 6:
        issued_books_rocord()

    elif choice == 7:
        returned_book_record()


    else:
        membership_record()
        
main()
