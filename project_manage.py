# import database module
import database
import os
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

    def create_project(self, db, Title, Member1, Member2, Advisor, Status='newly create'):
        self.user['role'] = "lead student"
        project_table = db.search("projects")
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

    def accept_invitation(self, db, ProjectID):
        self.user['role'] = "member student"
        member_pending_entry = {'ProjectID': ProjectID,
                                'to_be_member': self.ID,
                                'Response': "Accept",
                                'Response_date': str(datetime.datetime.now())}

        member_pending = db.search('Member_pending')
        member_pending.insert_entry(member_pending_entry)
        check_member = member_pending.filter(
            lambda x: x['ProjectID'] == ProjectID and x['Response'] == "Accept").select([])
        if len(check_member) == 2:
            project_table = db.search("projects")
            change_status = project_table.filter(
                lambda x: x['ProjectID'] == ProjectID).select([])
            for change in change_status:
                change['Status'] = "submittion"

    def deny_invitation(self, db, ProjectID):
        member_pending_entry = {'ProjectID': ProjectID,
                                'to_be_member': self.ID,
                                'Response': "Deny",
                                'Response_date': str(datetime.datetime.now())}

        member_pending = db.search('Member_pending')
        member_pending.insert_entry(member_pending_entry)

        project_table = db.search("projects")
        projects = project_table.filter(
            lambda x: x['ProjectID'] == ProjectID).select(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'])
        for project in projects:
            if project['Member1'] == user['ID']:
                project['Member1'] = ''

            if project['Member2'] == user['ID']:
                project['Member2'] = ''
            project_table.update(
                lambda x: x['ProjectID'] == ProjectID, project)


class Faculty:
    def __init__(self, user):
        self.ID = user['ID']
        self.Username = user['username']
        self.Password = user['password']
        self.type = user['role']
        self.user = user

    def accept_advisor(self, db, Project_ID):
        self.user['role'] = "advisor"
        invite_entry = {'ProjectID': Project_ID,
                        'to_be_advisor ': self.ID,
                        'Response': "Accept",
                        'Response_date': str(datetime.datetime.now())}

        Advisor_pending_request = db.search('Advisor_pending')
        Advisor_pending_request.insert_entry(invite_entry)
        project_table = db.search("projects")
        projects = project_table.filter(
            lambda x: x['ProjectID'] == Project_ID).select([])
        for project in projects:
            project['Status'] = 'evaluation'

    def deny_advisor(self, db, ProjectID):
        advisor_pending_entry = {'ProjectID': ProjectID,
                                 'to_be_member': self.ID,
                                 'Response': "Deny",
                                 'Response_date': str(datetime.datetime.now())}

        advisor_pending = db.search('Advisor_pending')
        advisor_pending.insert_entry(advisor_pending_entry)

        project_table = db.search("projects")
        projects = project_table.filter(
            lambda x: x['ProjectID'] == ProjectID).select(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'])
        for project in projects:
            project['Status'] = 'submittion fail'
            if project['Advisor'] == user['ID']:
                project['Advisor'] = ''
            project_table.update(
                lambda x: x['ProjectID'] == ProjectID, project)

    def accept_project(self, db, Project_ID):
        invite_entry = {'ProjectID': Project_ID,
                        'to_be_advisor ': self.ID,
                        'Response': " final approve",
                        'Response_date': str(datetime.datetime.now())}

        Advisor_pending_request = db.search('Advisor_pending')
        Advisor_pending_request.insert_entry(invite_entry)
        project_table = db.search("projects")
        projects = project_table.filter(
            lambda x: x['ProjectID'] == Project_ID).select([])
        for project in projects:
            project['Status'] = 'final approve'

    def deny_project(self, db, Project_ID):
        advisor_pending_entry = {'ProjectID': Project_ID,
                                 'to_be_member': self.ID,
                                 'Response': "evaluation fail",
                                 'Response_date': str(datetime.datetime.now())}

        advisor_pending = db.search('Advisor_pending')
        advisor_pending.insert_entry(advisor_pending_entry)

        project_table = db.search("projects")
        projects = project_table.filter(
            lambda x: x['ProjectID'] == Project_ID).select([])
        for project in projects:
            project['Status'] = 'evaluation fail'


class Admin:
    def __init__(self, user):
        self.ID = user['ID']
        self.Username = user['username']
        self.Password = user['password']
        self.type = user['role']


# define a function called exit


# save in exit function
def exit(db: database.DataBase):

    dict_field = {
        'login': ['ID', 'username', 'password', 'role'],
        'persons': ['ID', 'fist', 'last', 'type'],
        'projects': ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'],
        'Advisor_pending': ['ProjectID', 'to_be_advisor', 'Response', 'Response_date'],
        'Member_pending': ['ProjectID', 'to_be_member', 'Response', 'Response_date']}
    for table in db.database:
        filepath = os.getcwd() + "/" + table.table_name + ".csv"
        print(filepath)
        # open the file in the write mode
        f = open(filepath, 'w')  # relative path
        fields = dict_field[table.table_name]
        f.write(','.join(fields) + "\n")
        # # write a row to the csv file
        for row in table.table:
            f.write(','.join(row.values()) + "\n")

        f.close()


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
    print("2: for accept invitation or deny it")
    print("3: Exit")
    my_student = Student(user)
    user_choice = int(input("Select choice: "))
    if user_choice == 1:
        project_title = input("Input project Title: ")
        member1 = None
        while member1 == None:
            invite_member1 = input("Input id member1 for invitation: ")
            member1 = get_user_by_id(db, invite_member1)
            if member1 == None or member1["role"] != "student":
                print("User not found or invalid role")
                member1 = None

        member2 = None
        while member2 == None:
            invite_member2 = input("Input id member2 for invitation: ")
            member2 = get_user_by_id(db, invite_member2)
            if member2 == None or member2["role"] != "student" or member2 == member1:
                print("User not found or invalid role")
                member2 = None

        advisor = None
        while advisor == None:
            invite_advisor = input("Input id faculty to be advisor: ")
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
        if len(projects) == 0:
            print("You dont have any project invitation")
            sys.exit()
        ask = input("a(accept) or d(deny) or q(quit): ")

        if ask == "a":
            projectid = input("Project ID: ")
            my_student.accept_invitation(
                db, projectid)

        elif ask == "d":
            projectid = input("Project ID: ")
            my_student.deny_invitation(
                db, projectid)
        elif ask == "q":
            sys.exit()
        else:
            print("Invalid input")

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
        project_table = db.search('projects').filter(
            lambda x: x['Lead'] == user['ID']).select([])
        print(project_table)

    elif user_choice == 2:
        project_table = db.search('projects').filter(
            lambda x: x['Lead'] == user['ID'])
        member_pending_table = db.search('Member_pending')
        print(project_table.join(member_pending_table, "ProjectID").select([]))

    elif user_choice == 3:
        project_table = db.search('projects').filter(
            lambda x: x['Lead'] == user['ID'])
        advisor_pending_table = db.search('Advisor_pending')
        print(project_table.join(advisor_pending_table, "ProjectID").select([]))

    elif user_choice == 4:
        sys.exit()


elif user['role'] == 'member student':
    print("Option for member student")
    print("1: Display project table and edit")
    print("2: Exit")
    user_choice = int(input("Select choice: "))

    if user_choice == 1:
        project_table = db.search('projects').filter(
            lambda x: x['Member1'] == user['ID'] or x['Member2'] == user['ID'])
        member_pending_table = db.search('Member_pending')
        print(project_table.select([]))

    elif user_choice == 2:
        sys.exit()


elif user['role'] == 'faculty':
    print("Option for faculty")
    print("1: for accept invitation or deny it")
    print("2: Exit")
    our_faculty = Faculty(user)
    user_choice = int(input("Select choice: "))
    if user_choice == 1:
        """
        faculty will see the invitation after the group has two member already

        """
        filter_project_table = db.search("projects").filter(
            lambda x: x['Advisor'] == user['ID'] and x['Status'] == "submittion")
        projects = filter_project_table.select([])
        print(f"You have invite {len(projects)} projects")
        for row in projects:
            print(row['ProjectID'] + ": " + row['Title'])
        if len(projects) == 0:
            print("You dont have any project invitation")
            sys.exit()
        ask = input("a(accept) or d(deny) or q(quit): ")
        if ask == "a":
            projectid = input("Project ID: ")
            our_faculty.accept_advisor(
                db, projectid)

        elif ask == "d":
            projectid = input("Project ID: ")
            our_faculty.deny_advisor(
                db, projectid)
        elif ask == "q":
            sys.exit()

        else:
            print("Invalid input")

    elif user_choice == 2:
        sys.exit()


elif user['role'] == 'advisor':
    print("Option for advisor")
    print("1: Display project table and member_pending_table")
    print("2: Display advisor pending table")
    print("3: final approve")
    print("4: Exit")
    Advisor = Faculty(user)
    user_choice = int(input("Select choice: "))
    if user_choice == 1:
        """

        it will show after member1 and member2 accept invitation from lead student

        """
        project_table = db.search('projects').filter(
            lambda x: x['Advisor'] == user['ID'])
        member_pending_table = db.search('Member_pending')
        print(project_table.join(member_pending_table, "ProjectID").select([]))

    elif user_choice == 2:
        advisor_table = db.search('Advisor_pending').filter(
            lambda x: x['to_be_advisor'] == user['ID']).select([])
        print(advisor_table)

    elif user_choice == 3:

        filter_project_table = db.search("projects").filter(
            lambda x: x['Advisor'] == user['ID'] and x['Status'] == "evaluation")
        projects = filter_project_table.select([])
        print(f"You have {len(projects)} projects")
        for row in projects:
            print(row['ProjectID'] + ": " + row['Title'])
        if len(projects) == 0:
            print("You dont have any project for approve")
            sys.exit()
        ask = input("a(accept) or d(deny) or q(quit): ")
        if ask == "a":
            projectid = input("Project ID: ")
            Advisor.accept_project(
                db, projectid)

        if ask == "d":
            projectid = input("Project ID: ")
            Advisor.deny_project(
                db, projectid)

        if ask == "q":
            sys.exit()

    elif user_choice == 4:
        sys.exit()


elif user['role'] == 'admin':
    print("Option for admin")
    print("1: Display project table and edit")
    print("2: Display member pending table and edit")
    print("3: Display advisor pending table and edit")
    print("4: Delete table")
    print("5: Back up data")
    print("6: Exit")
    user_choice = int(input("Select choice: "))
    if user_choice == 1:
        project_table = db.search('projects').select([])
        print(project_table)

    elif user_choice == 2:
        member_pending_table = db.search('Member_pending').select([])
        print(member_pending_table)

    elif user_choice == 3:
        advisor_table = db.search('Advisor_pending').select([])
        print(advisor_table)

    elif user_choice == 4:
        print("1: Member_pending")
        print("2: Advisor_pending")
        print("3: Projects")
        select = int(input("Select table to delete: "))
        if select == 1:
            db.delete("Member_pending")
        elif select == 2:
            db.delete("Advisor_pending")
        elif select == 3:
            db.delete("projects")
        else:
            print("Invalid input")

    elif user_choice == 5:
        db_backup = database.DataBaseBackup()
        db_backup.getdata()

    elif user_choice == 6:
        sys.exit()


# input data to table for loop unitil the end then exit
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
