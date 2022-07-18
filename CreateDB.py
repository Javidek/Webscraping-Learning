import mysql.connector

def Create_db():
    userdb=input('Please enter a user for login DB:')
    passworddb=input('Please enter a password Login DB:')
    hostdb=input('Please enter a host database:')
    databasedb = 'Car'
    mydb=Authen_db(userdb,passworddb,hostdb)
    query=f'CREATE DATABASE {databasedb};'
    cursor=mydb.cursor()
    cursor.execute(query)
    query=f'USE {databasedb}'
    cursor=mydb.cursor()
    cursor.execute(query)
    query='CREATE TABLE Info_car ( Name varchar(20),Model varchar(20),Miles int,Accident int,Product_c int,Price int);'
    cursor=mydb.cursor()
    cursor.execute(query)
    return mydb
    
def Authen_db(userdb,passworddb,hostdb):
    mydb=mysql.connector.connect(
                                    user=userdb,
                                    password=passworddb,
                                    host=hostdb
                            )
    return mydb