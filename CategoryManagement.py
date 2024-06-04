# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:20:06 2023

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

class CategoryManagement:
    def __init__(self, class_a):
        #make a variable
        self.con=create_db_connection("localhost", "root", pw, db)
        self.class_a=class_a
        self.active_class=None
     
    #list of categories available in current active class
    def show_categories(self):
        active_class=self.class_a.show_class()
        #print(f"current active class: {active_class}")
        current_active_class_id=active_class[0][0]
        #print(current_active_class_id)
        if active_class is not None:
            query="select * from category where class_id={}".format(current_active_class_id)
            res=read_query(self.con, query)
            print()
            if len(res)!=0:
                df = pd.DataFrame(res, columns=['CATEGORY_ID', 'CATEGORY_NAME', 'WEIGHT', 'CLASS_ID'])
                pd.set_option('display.max_columns',None)
                pd.set_option('display.max_rows',None)
                print(df.to_string(index=False))
                return res
            else:
                print("No records found")
        else:
            print(f"There are no active classes")
    
    # add new categories
    def add_categories(self, category_name,weight):
        active_class=self.class_a.show_class()
        #print(active_class)
        current_active_class_id=active_class[0][0]
        #print(current_active_class_id)
        query = "SELECT * FROM category WHERE category_name=%s"
        existing_category = read_query(self.con, query,(category_name,))
        print()
        if active_class is not None:
            if len(existing_category)==0:
                query="insert into category(class_id, category_name, weight) values({}, '{}',{})".format(current_active_class_id,category_name, weight)
                execute_query(self.con, query)
                print("New Category is added!")
            elif len(existing_category):
                print(f"category: {category_name} already exists!!!")
        else:
            print("There are no active classes")
     
    #list all assignments present in the active class
    def show_assignments(self):
        active_class=self.class_a.show_class()
        #print(active_class)
        current_active_class_id=active_class[0][0]
        #print(current_active_class_id)
        if active_class is not None:
            query="""select category_id, assignment_name, assignment_desc,sum(points) as points_sum
            from assignment
            where class_id={}
            group by category_id, assignment_name,assignment_desc
            order by category_id""".format(current_active_class_id)
            res=read_query(self.con, query)
            print()
            if len(res)!=0:
                df = pd.DataFrame(res, columns=['CATEGORY_ID', 'ASSIGNMENT_NAME', 'ASSIGNMENT_DESC', 'POINTS_SUM'])
                pd.set_option('display.max_columns',None)
                pd.set_option('display.max_rows',None)
                print(df.to_string(index=False))
                return res
            else:
                print("No records found")
        else:
            print(f"There are no active classes")
            #for i in res:
                #print(i)
    
    #add new assignments in the categories
    def add_assignments(self, assignment_name, category_name,assignment_desc, points):
        active_class=self.class_a.show_class()
        #print(active_class)
        current_active_class_id=active_class[0][0]
        #print(current_active_class_id)
        if active_class is not None:
            #print("Hi")
            
            query="""select * from category where category_name='{}' and class_id='{}'
            """.format(category_name,current_active_class_id)
            res=read_query(self.con, query)
            #for i in res:
                #print(i)
            if res is not None:
                #print("There are records")
                current_category_id=res[0][0]
                #print(current_category_id)
                query = "SELECT * FROM assignment WHERE assignment_name=%s"
                existing_assignment = read_query(self.con, query,(assignment_name,))
                if len(existing_assignment)==0:
                    query1="""insert into assignment(assignment_name,category_id,class_id,assignment_desc,points) values('{}',{},{},'{}',{})                
                    """.format(assignment_name,current_category_id,current_active_class_id,assignment_desc,points)
                    execute_query(self.con, query1)
                    print("New assignment added!")
                elif len(existing_assignment)!=0:
                    print(f"Assignment: {assignment_name} already exists in {category_name} category")
            else:
                print("No records found!!!")
        else:
            print("There are no active classes")
        
        
        
#class_a=ClassManagement()
#cat_mgmt=CategoryManagement(class_a)
#cat_mgmt.show_categories()

#cat_mgmt.add_categories('Exams',0.3)
#cat_mgmt.add_assignments('Homework 1', 'Homeworks', 'E-R Diagrams', 100)
#cat_mgmt.show_assignments()
