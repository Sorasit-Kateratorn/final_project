# import database module
import database
import os
import csv
import random
import sys
import datetime

# define a funcion called initializing


def initializing():
    # here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program
    # create all the corresponding tables for those csv files
    login_table = database.read_csv_to_table("login", "login.csv")
    person_table = database.read_csv_to_table("persons", "persons.csv")
    db = database.DataBase()
    # add all these tables to the database
    # see the guide how many tables are needed
    db.insert(login_table)
    db.insert(person_table)
    return db


# define a funcion called login
# login no data for check user and password
# sensei only has store data for
def login(login_table):
    field_list = ["username", "password", "role"]
    # field_list = [] for see all field
    while True:
        user = input("Enter Username: ")
        pas1 = input("Enter password: ")
        # pass filter to check username and password from input
        filter_login_table = login_table.filter(
            lambda x: x['username'] == user and x['password'] == pas1)
        users = filter_login_table.select(field_list)
        if len(users) == 1:
            print("Welcome to our program")
            return users[0]

        else:
            print("Invalid username or password")

# here are things to do in this function:
   # add code that performs a login task
    # ask a user for a username and password
    # returns [ID, role] if valid, otherwise returning None

# define a function called exit


def exit(db: database.DataBase):
    dict_field = {
        'login': ['ID', 'username', 'password', 'role'],
        'persons': ['ID', 'fist', 'last', 'type']}
    for table in db.database:
        filepath = 'D:/IthXD/final_project/' + table.table_name + ".csv"
        print(filepath)
        # open the file in the write mode
        # f = open(filepath, 'w')  # relative path
        # note 'w' is there are another than w
        # create the csv writer
        # writer = csv.writer(f)
        fields = dict_field[table.table_name]
        # # write a row to the csv file
        print(fields)
        for row in table.table:
            print(row)
        # writer.writerow(row)
        # f.close()
        # myFile = open(filepath, 'r')
        # print("The content of the csv file is:")
        # print(myFile.read())
        # myFile.close()
    # insert_value = [{'ID': '7447677', 'username': 'Cristiano.R', 'password': '2255', 'role': 'admin'}, {'ID': '9898118', 'username': 'Lionel.M', 'password': '2977', 'role': 'student'}, {'ID': '5662557', 'username': 'Manuel.N', 'password': '1244', 'role': 'student'}, {'ID': '5687866', 'username': 'Robert.L', 'password': '8176', 'role': 'student'}, {'ID': '3557832', 'username': 'Gareth.B', 'password': '9462', 'role': 'student'}, {'ID': '2592572', 'username': 'Thibaut.C', 'password': '1985', 'role': 'student'}, {'ID': '1554306', 'username': 'Eden.H', 'password': '9106', 'role': 'student'}, {'ID': '4788888', 'username': 'Thiago.S', 'password': '5052', 'role': 'student'}, {'ID': '1863421', 'username': 'Sergio.R', 'password': '7228', 'role': 'student'}, {'ID': '4865631', 'username': 'Paul.P', 'password': '6956', 'role': 'student'}, {'ID': '7476758', 'username': 'Antoine.G', 'password': '6795', 'role': 'student'}, {'ID': '3938213', 'username': 'Marco.R', 'password': '8512', 'role': 'student'}, {'ID': '8382345', 'username': 'Toni.K', 'password': '7595', 'role': 'student'}, {
    #     'ID': '1042748', 'username': 'Mats.H', 'password': '1111', 'role': 'student'}, {'ID': '1228464', 'username': 'Hugo.L', 'password': '2193', 'role': 'student'}, {'ID': '4850789', 'username': 'Giorgio.C', 'password': '1201', 'role': 'student'}, {'ID': '5484541', 'username': 'Philipp.L', 'password': '4214', 'role': 'student'}, {'ID': '7998314', 'username': 'Gianluigi.B', 'password': '2351', 'role': 'student'}, {'ID': '5086282', 'username': 'Leonardo.B', 'password': '9413', 'role': 'student'}, {'ID': '8466074', 'username': 'Arjen.R', 'password': '6779', 'role': 'faculty'}, {'ID': '2567260', 'username': 'Paulo.D', 'password': '1312', 'role': 'faculty'}, {'ID': '8347432', 'username': 'Marco.V', 'password': '8780', 'role': 'faculty'}, {'ID': '4720327', 'username': 'David.A', 'password': '3861', 'role': 'faculty'}, {'ID': '7525643', 'username': 'Henrikh.M', 'password': '2636', 'role': 'faculty'}, {'ID': '2472659', 'username': 'Karim.B', 'password': '3828', 'role': 'faculty'}, {'ID': '1234567', 'username': 'Sorasit', 'password': '2014', 'role': 'student'}]
    # for value in insert_value:
    #     writer.writerow(value.values())
    # # close the file
    # f.close()
    # myFile = open('D:/IthXD/final_project/login.csv', 'r')
    # print("The content of the csv file is:")
    # print(myFile.read())
    # myFile.close()


# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files(5 table in database  person table, Login table, Project table, Advisor_pending_request table, Member_pending_request table)
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   # (key - id)
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python
# make calls to the initializing and login functions defined above
db = initializing()
# read csv to file and return type data base
# send db.search to function login
user = login(db.search("login"))

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
# see and do admin related activities
# elif val[1] = 'student':
# see and do student related activities
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit(db)
