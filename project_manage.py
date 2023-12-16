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
    my_csv = database.My_Csv()
    login_table = my_csv.read_csv_to_table("login", "login.csv")
    person_table = my_csv.read_csv_to_table("persons", "persons.csv")
    project_table = my_csv.read_csv_to_table("projects", "projects.csv")
    Advisor_pending_request = my_csv.read_csv_to_table(
        "Advisor_pending", "Advisor_pending.csv")
    Member_pending_request = my_csv.read_csv_to_table(
        "Member_pending", "Member_pending.csv")
    db = database.DataBase()
    # add all these tables to the database
    # see the guide how many tables are needed
    db.insert(login_table)
    db.insert(person_table)
    db.insert(project_table)
    db.insert(Advisor_pending_request)
    db.insert(Member_pending_request)
    return db


# define a funcion called login
# login no data for check user and password
# sensei only has store data for
def login(login_table):
    # field_list = ["username", "password", "role"]
    field_list = []  # for see all field
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


class Student:
    def __init__(self, user):
        self.ID = user['ID']
        self.Username = user['username']
        self.Password = user['password']
        self.type = user['role']
        self.user = user

    # ProjectID,Title,Lead,Member1,Member2,Advisor,Status
    def create_project(self, db, Title, Member1, Member2, Advisor, Status='newly create'):
        self.user['role'] = "lead student"
        project_table = db.search("projects")
        # Member_pending_table = db.search("Member_pending")
        # Advisor_pending_table = db.search("Advisor_pending")
        Project_ID = str(len(project_table.table) + 1)
        project_entry = {
            'ProjectID': Project_ID,
            'Title': Title,
            'Lead': self.ID,
            'Member1': Member1,
            'Member2': Member2,
            'Advisor': Advisor,
            'Status': Status}
        project_table.insert_entry(project_entry)

        # Member1_entry = {'ProjectID': Project_ID,
        #                  'to_be_member': Member1}
        # Member2_entry = {'ProjectID': Project_ID,
        #                  'to_be_member': Member2}

        # Member_pending_table.insert_entry(Member1_entry)
        # Member_pending_table.insert_entry(Member2_entry)

        # Advisor_entry = {'ProjectID': Project_ID,
        #                  'to_be_advisor': Advisor}  # ProjectID,to_be_advisor,Response,Response_date

        # Advisor_pending_table.insert_entry(Advisor_entry)

        # create new record in project table

    # ProjectID,to_be_member,Response,Response_date
    def accept_invitation(self, Member_pending_table, ProjectID):
        self.user['role'] = "member student"
        member_pending_entry = {'ProjectID': ProjectID,
                                'to_be_member': self.ID,
                                'Response': "Accept",
                                'Response_date': str(datetime.datetime.now())}

        Member_pending_table.insert_entry(member_pending_entry)

    # deny select exit == deny
    # def deny_invitation(self, member_pending_table):
    #     # Assuming member_pending_table has columns like 'project_id' and 'student_id'
    #     pending_entries = member_pending_table.filter(
    #         lambda entry: entry['student_id'] == self.ID)
    #     if pending_entries:
    #         # Assuming there is only one pending invitation for simplicity
    #         member_pending_table.table.remove(pending_entries[0])
    #         print(f"Invitation denied for student with ID {self.ID}.")
    #     else:
    #         print("Error: No pending invitations found.")
    # # update member pending table response = deny

    # ProjectID,to_be_advisor,Response,Response_date

    def invite_advisor(self, Advisor_pending_request, Response, Response_date=datetime.datetime.now()):
        self.type = "lead student"
        invite_entry = {'ProjectID': str(len(Advisor_pending_request.table) + 1),
                        'Response': Response,
                        'Response_date': Response_date}

        Advisor_pending_request.insert_entry(invite_entry)

    def __str__(self):
        return f"Student(ID: {self.ID}, Username: {self.Username}, Type: {self.type}, Project_ID: {self.Project_ID})"


class Faculty:
    def __init__(self, user):
        self.ID = user['ID']
        self.Username = user['username']
        self.Password = user['password']
        self.type = user['role']

    # ProjectID,to_be_advisor,Response,Response_date
    def accept_advisor(self, Advisor_pending_request, Response, Response_date=datetime.datetime.now()):
        self.type = "lead student"
        invite_entry = {'ProjectID': str(len(Advisor_pending_request.table) + 1),
                        'Response': Response,
                        'Response_date': Response_date}

        Advisor_pending_request.insert_entry(invite_entry)

    # def deny_invitation(self, Advisor_pending_request):
    #     pending_entries = Advisor_pending_request.filter(
    #         lambda entry: entry['faculty_id'] == self.ID)
    #     if pending_entries:
    #         # Assuming there is only one pending invitation for simplicity
    #         Advisor_pending_request.table.remove(pending_entries[0])
    #         print(f"Invitation denied for advisor with ID {self.ID}.")
    #     else:
    #         print("Error: No pending invitations found.")
    # # update Adisor pending table response = deny

        def __str__(self):
            return f"Faculty(ID: {self.ID}, Username: {self.Username}, Type: {self.type}"


class Admin:
    def __init__(self, user):
        self.ID = user['ID']
        self.Username = user['username']
        self.Password = user['password']
        self.type = user['role']

    def delete(self):
        pass


# define a function called exit


# save in exit function
def exit(db: database.DataBase):
    """
    change your file path to write the file all file must in the same folder

    """

    dict_field = {
        'login': ['ID', 'username', 'password', 'role'],
        'persons': ['ID', 'fist', 'last', 'type'],
        'projects': ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'],
        'Advisor_pending': ['ProjectID', 'to_be_advisor', 'Response', 'Response_date'],
        'Member_pending': ['ProjectID', 'to_be_member', 'Response', 'Response_date']}
    for table in db.database:
        filepath = 'D:/IthXD/final_project/' + table.table_name + ".csv"
        print(filepath)
        # open the file in the write mode
        f = open(filepath, 'w')  # relative path
        fields = dict_field[table.table_name]
        f.write(','.join(fields) + "\n")
        # # write a row to the csv file
        # print(','.join(fields))
        for row in table.table:
            f.write(','.join(row.values()) + "\n")
            # print(','.join(row.values()))
        f.close()
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


def get_user_by_id(db, id):
    login_table = db.search("login")
    filter_login_table = login_table.filter(
        lambda x: x['ID'] == id)
    users = filter_login_table.select([])  # select all field
    if len(users) == 1:
        return users[0]
    else:
        return None


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
# print(user)

if user['role'] == 'student':  # create project and accept project from invite
    print("Option for student")
    print("1: for create project")
    print("2: for accept invitation")
    print("3: Exit")
    print("4: Display project")
    my_student = Student(user)
    user_choice = int(input("Select choice: "))
    if user_choice == 1:
        project_title = input("Input project Title: ")
        member1 = None
        while member1 == None:
            invite_member1 = input("Input id member1: ")
            member1 = get_user_by_id(db, invite_member1)
            if member1 == None or member1["role"] != "student":
                print("User not found or invalid role")
                member1 = None

        member2 = None
        while member2 == None:
            invite_member2 = input("Input id member2: ")
            member2 = get_user_by_id(db, invite_member2)
            if member2 == None or member2["role"] != "student" or member2 == member1:
                print("User not found or invalid role")
                member2 = None

        advisor = None
        while advisor == None:
            invite_advisor = input("Input advisor: ")
            advisor = get_user_by_id(db, invite_advisor)
            if advisor == None or advisor["role"] == "student":
                print("User not found or invalid role")
                advisor = None

        my_student.create_project(
            db, project_title, member1['ID'], member2['ID'], advisor['ID'])

    elif user_choice == 2:  # ID find in field project table filter student id
        filter_project_table = db.search("projects").filter(
            lambda x: x['Member1'] == user['ID'] or x['Member2'] == user['ID'])
        projects = filter_project_table.select([])
        print(f"You have invite {len(projects)} projects")
        for row in projects:
            print(row['ProjectID'] + ": " + row['Title'])
        ask = input("Project ID or q(quit): ")
        if ask != "q":
            my_student.accept_invitation(db.search("Member_pending"), ask)

    elif user_choice == 3:
        sys.exit()


elif user['role'] == 'lead student':
    print("Option for lead student")
    print("1: Display project table and edit")
    print("2: Display member pending table")
    print("3: Display advisor pending table")
    print("4: Exit")
    user_choice = int(input("Select choice: "))

    if user_choice == 1:
        pass
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        pass
    elif user_choice == 4:
        sys.exit()


elif user['role'] == 'member student':
    print("Option for member student")
    print("1: Display project table and edit")
    print("2: Exit")
    user_choice = int(input("Select choice: "))

    if user_choice == 1:
        pass

    elif user_choice == 2:
        sys.exit()


elif user['role'] == 'faculty':
    print("Option for faculty")
    print("1: Display project table")
    print("2: Display advisor pending table")
    print("3: for accept invitation")
    print("4: Exit")
    user_choice = int(input("Select choice: "))
    if user_choice == 1:
        pass

    elif user_choice == 2:
        pass

    elif user_choice == 3:
        pass

    elif user_choice == 4:
        sys.exit()


elif user['role'] == 'advisor':
    print("Option for advisor")
    print("1: Display project table")
    print("2: Display advisor pending table")
    print("3: Exit")
    user_choice = int(input("Select choice: "))
    if user_choice == 1:
        project_table = db.search('projects').filter(
            lambda x: x['Advisor'] == user['ID'])
        member_pending_table = db.search('Member_pending')
        # project_table.join(member_pending_table, "ProjectID").select([])
        print("ABC")
        print(project_table.join(member_pending_table, "ProjectID").select([]))

    elif user_choice == 2:
        pass

    elif user_choice == 3:
        pass

    elif user_choice == 4:
        sys.exit()


elif user['role'] == 'admin':
    print("Option for admin")
    print("1: Display project table and edit")
    print("2: Display member pending table and edit")
    print("3: Display advisor pending table and edit")
    print("4: Delete table")
    print("5: Exit")
    user_choice = int(input("Select choice: "))
    if user_choice == 1:
        pass
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        pass
    elif user_choice == 4:
        db.delete("Member_pending")

    elif user_choice == 5:
        sys.exit()


# input data to table for loop unitil the end then exit
# table_login = db.search("login")
# userA = {"ID": "10234", "username": "Sorasit",
#          "password": "2014", "role": "student"}

# table_login.insert_entry(userA)
# my_student = Student("6610545944", "Sorasit", " 1234", "student")
# my_student.create_project(db.search("projects"), "Final")

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
