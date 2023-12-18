# Final project for 2023's 219114/115 Programming I

## **`A list of files`**

**1) database.py**:

use to create tables

**2) project_manage.py**:

main program to run

**3) Proposal.md**:

explain evaluation step

**4) TODO.md**:

explain function and role in this program

**5) Advisor_pending.csv**:

store data respone from faculty and advisor

**6) Member_pending.csv**:

store data respone from student and member student

**7) projects.csv**:

store project data

**8) login.csv**:

store data for user 

**9) persons.csv**:

store data for user

**10) README.md**:

breif description describing what classes each of the files contains and what purposes do these classes serve.


## **`A description on how to compile and run your project.`**

*   run project_manage.py (use username and password from login.csv)



## **`A table detailing each role and its actions`**

| Role                   | Action         | Method                            | Class           | Completion  percentage |
|------------------------|----------------|-----------------------------------|-----------------|------------------------|
| Admin                  | delete data    | delete                            | DataBase, Table | 100%                   |
| Admin                  | backup data    | getdata                           | DataBaseBackup  | 100%                   |
| Admin                  | view table     | search                            | DataBase, Table | 100%                   |
| Student change to Lead | create project | create_project                    | Student         | 100%                   |
| Student change to Lead | invitation     | get_user_by_id                    | DataBase, Table | 100%                   |
| Student                | accept or deny | accept invitation deny invitation | Student         | 100%                   |
| Member                 | view project   | search                            | DataBase, Table | 100%                   |
| Faculty                | accept or deny | accept advisor deny advisor       | Faculty         | 100%                   |
| Advisor                | accept or deny | accept project deny project       | Faculty         | 100%                   |
| Advisor                | view table     | search                            | DataBase, Table | 100%                   |



## **`A list of missing features`**

* Can't edit username and password   (You can't access the program if you dont have username and password in login.csv)

* Can't change title name in project (Once you create it already)

* role can't change back (if you accept the invitation already)
