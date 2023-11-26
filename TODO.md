# **Person table link with login table by id**
## **`Student Role`**
**Objective**: The student role involves tasks related to managing their own information and projects.


**1) View Personal Information**:

Display the student's personal information such as ID, first name, last name, and role.

**2) View Assigned Projects**:

Retrieve and display a list of projects assigned to the student.

**3)Update Personal Information**:

Allow the student to update their personal information (e.g., first name, last name).


# **`Member student`**
**1) Update and modify project**:

See and modify his project details (Title and field for evaluation)


# **`lead student`**

**1) Create a project**: Create new project ID for your group 
(inilization for your project ID and find your members and advisor use project table that link data with person table)

**2) Find members**: invite new member for your project group

(use Person table and Member_pending_request table for store this data)

**3) Send invitational messages to potential members**:
student can see your invitational messages and select accept or decline.
(use person table for store data type that is faculty)

**4) Add members to the project and form a group**:

(use project table that link data with Member_pending_request table
and update in person table type)

**5) See and modify his own project details**: 

(use project table for store data)

**6) Send request messages to potential advisors**:

(use Advisor_pending_request table to store this data)

**7) Submit the final project report**:

(submit project table and change status to submitting)

# `**create status in this project table**`
*   Newly create(no member, no value in advisor yet)
*   Submitting (full member and advisor)
*   Evaluating (approve after submittion)
*   Final approve(after pass evaluation)



## **`Faculty Role`**
**Objective**:
The faculty role involves tasks related to managing student information, approving/rejecting projects, and updating their own information.

**1) View Student Information:**

Display a list of student information including ID, first name, last name, and role.

**2) Approve/Reject Projects**:

Retrieve and display a list of project proposals submitted by students.
Allow the faculty to approve or reject project proposals.

**3) Update Personal Information**:

Allow the faculty to update their personal information (e.g., first name, last name).



## **`Advisor Role`**
**Objective**:
Advisor role consider project and give an advise for improve project.

**1) See request to be a supervisor**: (if accept it your role will change from faculty to advisor)

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

**3) Change User Roles**:

Allow the admin to change the roles of users (e.g., change a student to a faculty member).

**4) Delete User**:

Allow the admin to delete a user from the system.

**5) View Project Information**:

Retrieve and display information about all projects.

**6) Update Project Status**:

Allow the admin to update the status of projects (e.g., mark a project as completed).

**7) Update Admin Information**:

Allow the admin to update their personal information (e.g., first name, last name).
## **`General Notes:`**
**User Authentication**:

Implement a login system for each role with appropriate authentication mechanisms.

**Database Operations**:

Define functions for database operations such as adding tables, retrieving tables, updating entries, etc.

**Input Validation**:

Implement input validation to ensure data integrity and security.

**Logging**:

Implement logging mechanisms to track important system activities.