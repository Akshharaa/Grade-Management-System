# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:49:32 2023

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

class GradeReporting:
    def __init__(self, class_a):
        #make a variable
        self.con=create_db_connection("localhost", "root", pw, db)
        self.class_a=class_a
        self.active_class=None
        
    # lists students assignmetns and grades and the percentage of points in each category
    def student_grades(self,username):
        active_class = self.class_a.show_class()
        print()
        if active_class is not None:
            current_active_class_id = active_class[0][0]
            #print(f"current_active_class_id: {current_active_class_id}")
            query="""select category_name, group_concat(assignment_name,':',grade) as assignments, sum(grade) as attempted_points, sum(points) as total_possible_points, (sum(grade)/sum(points))*100 as fraction_of_points
                from(
                select assignment.class_id,student.student_id,student.student_name,student.username,category.category_name,assignment.assignment_name, COALESCE(grade.grade, 'Not graded') AS grade, assignment.points
                from category
                left join assignment on category.category_id=assignment.category_id
                left join grade on grade.assignment_id=assignment.assignment_id
                left join student on student.student_id=grade.student_id
                where student.username='{}' and assignment.class_id={}) as subq1
                group by category_name
            """.format(username,current_active_class_id)
            res=read_query(self.con, query)
            #for i in res:
                #print(i)
            if len(res)!=0:
                df = pd.DataFrame(res, columns=['CATEGORY_NAME', 'ASSIGNMENTS','ATTEMPTED_POINTS','TOTAL_POSSIBLE_POINTS','FRACTION OF POINTS'])
                pd.set_option('display.max_columns',None)
                pd.set_option('display.max_rows',None)
                print(df.to_string(index=False))
            else:
                print(f"There are no records for {username} in class: {current_active_class_id}")
            #print(res)
        else:
            print("There is no active class")
    
    #lists the total grades of all students whose grades are available
    def gradebook(self):
        active_class = self.class_a.show_class()
        print()
        if active_class is not None:
            current_active_class_id = active_class[0][0]
            query="""select student_id, student_name, username, (sum(grade)/sum(points))*100 as total_grade
                from(
                select assignment.class_id,student.student_id,student.student_name,student.username,category.category_name,assignment.assignment_name, COALESCE(grade.grade, 'Not graded') AS grade, assignment.points
                from category
                left join assignment on category.category_id=assignment.category_id
                left join grade on grade.assignment_id=assignment.assignment_id
                left join student on student.student_id=grade.student_id
                where assignment.class_id={}) as sub1
                group by student_id;
            """.format(current_active_class_id)
            res=read_query(self.con, query)
            #for i in res:
                #print(i)
            if len(res)!=0:
                df = pd.DataFrame(res, columns=['STUDENT_ID', 'STUDENT_NAME','USERNAME','TOTAL_GRADE'])
                pd.set_option('display.max_columns',None)
                pd.set_option('display.max_rows',None)
                print(df.to_string(index=False))
            else:
                print(f"There are no records in class: {current_active_class_id}")
            #print(res)
        else:
            print("There is no active class")
        
                
                
                
                
#class_a=ClassManagement()
#gr=GradeReporting(class_a)
#gr.grades('hasserb')

#gr.gradebook()

