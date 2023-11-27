# **`Thing has to do`**


*   Modularization
*   Testcase

*   Clean code
*   Modularization


# **`Evaluation step`** 

1) lead student has to send a request to member1 and member2 after member accept the request (use person table) (status "newly create" in project table)

2) lead student send a request to faculty for advisor (if faculty denies lead student has to send a request to other faculty) (status "newly create" in project table)

3) after accept invitation (This program will store id in project table) (status "submittion")

4) after submittion this program will add record in Advisor_pending_request for approve submittion project(Advisor select approve or not for this title project)

5) if advisor deny lead student and member has to change title project until advisor approve (status "submittion fail" in project table)

6) after advisor approve (status "evaluation" in project table)

7) update field text (under project table) (status "first evaluation")

8) send to advisor (create record in Advisor_pending_request)

9) if advisor deny it will update status "first evaluation fail"

10) lead student and member recieve a request to update field text

11) send back to advisor  (status "second evaluation")

12) loop continue until advisor approve (using count for this loop)

13) if advisor approve (status "final approve" in project table)

**How to know difference between evaluation and final approve**

add one more field such ad file(empty in status 'create and submmition' member and lead student will modify in this state) (approve advisor  ) and text in project table (field text in python)