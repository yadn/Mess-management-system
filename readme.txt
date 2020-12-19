CS699:Project- Mess Management System

Team name :  Technocrats
Members:

Name                    Roll no.          contribution

Ashish Kumar Goyal     193050058          Integration of UI and Databases
Aman Kumar Singh       193050022          databases, report and user roles 
Yadnyesh Patil         193050067          User Interface and Databases

Motivation:

1.The current process of applying for rebates is not very clear and
hence most of the students just don’t apply for it which in turn
wastes food,money etc.

2.If the mess workers know the number of students that are going to
miss the meal, it will be easy for them to estimate the amount of
food to be made.

3.The record of students are stored on a register, one page for each
student and most of the time these pages go blank at the end of
the month. This incurs a lot of wastage of paper which can be
easily avoided.

4. The effort for creating the mess bills of all the students at the end
of the month is a tedious task which can very well be made easy
using the app.Less efforts and better results for every one

Git link of the project:

https://github.com/yadn/Mess-management-system


How to run the webapp:

1.install django
2.Go to the required folder
3.run server: python3 manage.py runserver
4.A link to local server will be shown .
5. Go to that link.
6.webapp will be launched.
7.Log into the webapp using different users. credentials are given below.



run migrations: python3 manage.py makemigrations
                python3 manage.py migrate

load initial data: python3 manage.py loaddata initial.fixtures

superuser credentials:
    username- sysad
    password- messadmin

Mess manager credentials:
    username- h4_manager
    password- messofh4

Mess worker credentials:
    username- mess_worker
    password- h4worker

Student credentials:
    username:  [193050003,193050022,193050058,193050059,193050067]
    password: student

--STUDENT---

viewreq.html = view status of requests made by students (rebates request table to be added) also the homepage for students

rebates.html = apply for rebates

overheads.html = apply for overheads

--Mess worker--

appreq.html = approve overhead requests mae by students, this is also the homepage for mess workers

todaycount.html = shows today's total number of meals in each session and in total

counthistory.html = shows history of overhead requests of students and history of daily count

--Mess Manager--

apprebate.html = approve reabates (will be done by mess manager) also the homepage for him

setmealprice.html = to edit price of a meal (date feature can be added)

monthlyrepo.html = shows current month report

dailyreqhist.html = History of overhead requests

References:
https://oldcc.iitb.ac.in/engfaqgeneinf/engldap
https://django-auth-ldap.readthedocs.io/en/latest/
https://www.tldp.org/HOWTO/LDAP-HOWTO/authentication.html
https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Introduction
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
https://www.overleaf.com/articles/literature-review-for-energy-consumption-in-manufacturing-industry-from-machine-to-factory-level/kxzppvnczqxm
