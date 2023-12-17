# **For run this programm user must have data (such as username, password and role) in login.csv**

# **Person table link with login table by id**
## **`Student Role`**
**Objective**: The student role involves tasks related to managing their own information and projects.


**1) View Assigned Projects**:

Retrieve and display a list of projects assigned to the student.

**2) Accept or Deny Projects**:

Allow student to accept or deny projects.


# **`Member student`**

Member student is a student that accept the invitation to project (role student will change to member student in Login table)

**1) Update and modify project**:

See and modify his project details (Title and field for evaluation)


# **`lead student`**

lead student is a student that create a project (role student will change to lead student in Login table)

**1) Create a project**: Create new project ID for your group 
(inilization for your project ID and find your members and advisor use project table that link data with id from Login table)

**2) Find members**: invite new member for your project group

(use Login table and Member_pending_request table for store this data)

**3) Send invitational messages to potential members**:
student can see your invitational messages and select accept or decline.
(use person table for store data type that is faculty)

**4) Add members to the project and form a group**:

(use project table that link data with Member_pending_request table
and update in person table type)

**5) See and modify his own project details**: 

(use Project table for store data)

**6) Send request messages to potential advisors**:

(use Advisor_pending_request table to store this data)

**7) Submit the final project report**:

(submit Project table and change status to submitting)

# `**create status in this project table**`
*   Newly create(no member, no value in advisor yet)
*   Submittion (full member)
*   Final approve(after pass evaluation)



## **`Faculty Role`**
**Objective**:
The faculty role involves tasks related to approving/rejecting projects, and updating their own information.

**1) Approve/Reject Projects**:

Retrieve and display a list of project proposals submitted by students.
Allow the faculty to approve or reject project proposals.


## **`Advisor Role`**
**Objective**:
Advisor role consider project and give an advise for improve project (can give an advise more than 1 project).

**1) See request to be a supervisor**: (if accept it your role will change from faculty to advisor in login table)

**2) Send accept response**: (for projects eventually serving as an advisor)
 
 (use Advisor_pending_request table for store this information)

**3) Send deny response**: (for projects not eventually serving as an advisor)
 
 (use Advisor_pending_request table for store this information)

**4) See details of all the project**: (project table)

**5) Evaluate projects**: (explain in propproposal)

**6) Approve the project**: (change status in project table to final approve)



## **`Admin Role`**
**Objective**:
The admin role involves tasks related to initializing the system, managing user information, and overseeing the overall functionality.

**1) System Initialization**:

Read data from an input CSV file to initialize the system.
Create and populate the 'persons' table.
Create and populate the 'login' table.

**2) View All User Information**:

Retrieve and display a list of all user information, including students and faculty.

**3) Delete data**:

Allow the admin to delete data from the system. (delete data in login, Member_pending, Advisor_pending and projects table)

**4) View information in all table**:

Retrieve and display information about all projects.

**5) Update user Information**:

Allow the admin to update user personal information in person table (e.g., first name, last name).

**6) Database Operations**:

Define functions for database operations such as adding tables, retrieving tables, updating entries, back up, etc.



## **`General Notes:`**
**User Authentication**:

Implement a login system for each role with appropriate authentication mechanisms.

**Input Validation**:

Implement input validation to ensure data integrity and security.

**Logging**:

Implement logging mechanisms to track important system activities.