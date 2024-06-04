# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:19:38 2023

@author: thari
"""

import connection
from connection import create_server_connection as create_server_connection
from connection import create_db_connection as create_db_connection
from connection import execute_query
from connection import read_query
from ClassManagement import ClassManagement
import mysql.connector as connector
from mysql.connector import Error
import pandas as pd


pw='@Jerry1243'
db = "school_mgmt"
con = create_server_connection("127.0.0.1", "root", pw)

class StudentManagement:
    def __init__(self,class_a):
        #make a variable
        self.con=create_db_connection("localhost", "root", pw, db)
        self.class_a=class_a
        self.active_class=None
        

    #add a new student to the database and enroll in the current active class
    def add_student(self, username, student_id, first, last):
        query = "SELECT * FROM student WHERE username=%s"
        current_student = read_query(self.con, query,(username,))
        #print(current_student)
        #print(len(current_student))
        
       
        active_class = self.class_a.show_class()
        print()
        name=f"{first} {last}"
        if active_class is not None:
            current_active_class_id = active_class[0][0]
            #print(f"current_active_class_id: {current_active_class_id}")
            if len(current_student)==0:
                #print("Hello")
                #add the new student in students and enroll in the current active class
                #add the student
                
                query1="insert into student(student_id,student_name,username) values({},'{}','{}')".format(student_id, name,username)
                execute_query(self.con, query1)
                print("New Student added")
                #Enroll the student
                query2="""insert into enroll(class_id, student_id) values({},{})
                """.format(current_active_class_id,student_id)
                execute_query(self.con,query2)
                print("New student enrolled in class")
            elif len(current_student)!=0:
                current_student_id=current_student[0][0]
                #print(f"current_student_id: {current_student_id}")
                #print(current_student[0][1])
                if name!=current_student[0][1]:
                    query3="""update student set student_name='{}' where username='{}'
                    """.format(name,username)
                    execute_query(self.con,query3)
                    print("WARNING!!! There is a change in the student name")
                else:
                    print("There is no chnage in the name")
        else:
            print("There are no active classes.")
        
    #enrolling an already existing student if exists
    def add_student1(self, username):
        query = "SELECT * FROM student WHERE username=%s"
        current_student = read_query(self.con, query,(username,))
        #print(current_student)
        #print(len(current_student))
        active_class = self.class_a.show_class()
        print()
        #current_active_class_id = active_class[0][0]
        #print(f"current_active_class_id: {current_active_class_id}")
        if active_class is not None:
            current_active_class_id = active_class[0][0]
            #print(f"current_active_class_id: {current_active_class_id}")
            if len(current_student)!=0:
                current_student_id=current_student[0][0]
                #print(f"current_student_id: {current_student_id}")
                #print("Enroll the student in this class")
                query1="""insert into enroll(class_id, student_id) values({},{})
                """.format(current_active_class_id,current_student_id)
                execute_query(self.con,query1)
                print("New student enrolled in class")
            elif len(current_student)==0:
                print("There is no such student. Add the student and then enroll in a class")
        else:
            print("There are no active classes.")
            
    
    #list all the students present int he active class
    def show_students(self):
        active_class = self.class_a.show_class()
        print()
        if active_class is not None:
            current_active_class_id = active_class[0][0]
            #print(f"current_active_class_id: {current_active_class_id}")
            query="""select student.student_id, student.student_name , student.email
            from student
            inner join enroll on enroll.student_id=student.student_id
            where enroll.class_id={}
            """.format(current_active_class_id)
            res=read_query(self.con, query)
            #for i in res:
                #print(i)
            #print(res)
            if len(res)!=0:
                df = pd.DataFrame(res, columns=['STUDENT_ID', 'STUDENT_NAME','EMAIL_ID'])
                pd.set_option('display.max_columns',None)
                pd.set_option('display.max_rows',None)
                print(df.to_string(index=False))
               #if res:
            
            else:
                print("No records found!!!")
            #print(res)
        else:
            print("There are no active classes.")
    
    #list all the students with the given string in student_name and username
    def show_students1(self,string):
        search_string=f'%{string}%'
        active_class = self.class_a.show_class()
        print()
        if active_class is not None:
            current_active_class_id = active_class[0][0]
            #print(f"current_active_class_id: {current_active_class_id}")
            query="""select student.student_id, student.student_name , student.username
            from student
            inner join enroll on enroll.student_id=student.student_id
            where enroll.class_id=%s and (student.student_name like %s or student.username like %s)
            """
            res=read_query(self.con, query, (current_active_class_id, search_string, search_string))
            if len(res)>0:
                df = pd.DataFrame(res, columns=['STUDENT_ID', 'STUDENT_NAME', 'USERNAME'])
                pd.set_option('display.max_columns',None)
                pd.set_option('display.max_rows',None)
                print(df.to_string(index=False))
            else:
                print("No such records found!")
        else:
            print("There are no active classes.")
    
    #assigning grades to the student for the assignments
    def grades(self, assignment_name,username,grade):
        active_class = self.class_a.show_class()
        print()
        if active_class is not None:
            current_active_class_id = active_class[0][0]
            #print(f"current_active_class_id: {current_active_class_id}")
            #print("Hi")
            query="""select * from assignment where assignment_name='{}' and class_id={}
            """.format(assignment_name,current_active_class_id)
            assignment_result=read_query(self.con, query)
           # print(assignment_result)
            #print(len(assignment_result))
            if len(assignment_result)!= 0:
                if grade>assignment_result[0][5]:
                    print(f"WARNING!!! The configured points for the assignment: {assignment_name} are {assignment_result[0][5]}")
                    print()
                current_assignment_id=assignment_result[0][0]
                #print(f"current_assignment_id: {current_assignment_id}")
                #check if the student exists
                query1="""select student.student_id, student.student_name, student.username
                from student
                inner join enroll on student.student_id=enroll.student_id
                where student.username='{}' and enroll.class_id={}
                """.format(username,current_active_class_id)
                student=read_query(self.con, query1)
                #for i in student:
                    #print(f"student: {i}")
                    
                if student:
                    current_student_id=student[0][0]
                    #print(f"current_student_id: {current_student_id}")
                    
                    query2="""select * from grade where student_id={} and assignment_id={}
                    """.format(current_student_id,current_assignment_id)
                    existing_grade=read_query(self.con, query2)
                    
                    if existing_grade:
                        #print("Hi")
                        #print("There is an existing record")
                        #for i in existing_grade:
                           #print(i)
                        if len(existing_grade)>0:
                            df = pd.DataFrame(existing_grade, columns=['GRADE_ID', 'STUDENT_ID', 'ASSIGNMENT_ID', 'GRADE'])
                            pd.set_option('display.max_columns',None)
                            pd.set_option('display.max_rows',None)
                            print(df.to_string(index=False))
                        else:
                            print("No such records found!")
                    
                        #print("existing grade not Null")
                        query3="""update grade set grade={} where student_id={} and assignment_id={}
                        """.format(grade,current_student_id,current_assignment_id)
                        updated_grade=execute_query(self.con, query3)
                        print("The grade is updated")
                    else:
                        #print("Hello")
                        print(f"There is no record for the student: {username} in grade")
                        query4="""insert into grade(student_id,assignment_id,grade) values({},{},{})
                        """.format(current_student_id,current_assignment_id,grade)
                        added_grade=execute_query(self.con, query4)
                        print("New record added in grade")
                else:
                    print(f"There are no records for student_username:{username} in class:{current_active_class_id}")
            elif len(assignment_result)==0:
                print(f"There are no records available for {assignment_name} in class:{current_active_class_id}")
        else:
            print("There are no active classes")
                    
                    
    
   
        
        
            
            

                
#class_a=ClassManagement()
#sm=StudentManagement(class_a)

#sm.add_student('abc', 1,'abc','abcd')
#sm.add_student('pqr', 31,'pqr','stu')
#sm.add_student('a', 32, 'a', 'b')

#sm.add_student1('hasserb')

#sm.show_students()

#sm.show_students1('a')
#sm.show_students1('ab')
#sm.show_students1('hasser')
#sm.show_students1('ammy')

#sm.grades('Homework 1','hasserb',93)
#sm.grades('Homework 2','hasserb',0)
#sm.grades('Midterm 1','hasserb',80)
#sm.grades('Midterm 2','hasserb',85)
#sm.grades('Final Exam','hasserb',100)




