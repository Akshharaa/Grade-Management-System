# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:20:59 2023

@author: thari
"""

import connection
from connection import create_server_connection as create_server_connection
from connection import create_db_connection as create_db_connection
from connection import execute_query
from connection import read_query
import mysql.connector as connector
from mysql.connector import Error
import pandas as pd


pw='@Jerry1243'
db = "school_mgmt"
con = create_server_connection("127.0.0.1", "root", pw)

class ClassManagement:
    def __init__(self):
        #make a variable
        self.con=create_db_connection("localhost", "root", pw, db)
        
    #creating a new class 
    def create_class(self, course_code, term, section_num, class_desc):
        query="insert into class(course_code, term, section_num, class_desc) values('{}', '{}', {}, '{}')".format(course_code, term, section_num, class_desc)
        execute_query(self.con, query)
        print("New class is created")
    
    #list of classes available
    def list_class(self):
        query="""select class.class_id, class.course_code, class.class_desc, class.section_num,count(enroll.student_id) as num_of_students from class
        left join enroll on class.class_id = enroll.class_id
        group by class.class_id;;
        """
        res=read_query(self.con, query)
        if len(res)!=0:
            df = pd.DataFrame(res, columns=['CLASS_ID', 'COURSE_ID','CLASS_DESC','SECTION_NUM', 'NUM_OF_STUDENTS'])
            pd.set_option('display.max_columns',None)
            pd.set_option('display.max_rows',None)
            print(df.to_string(index=False))
        else:
            print(f"There are no records available")

    
   # activating a class
    def select_class(self, course_code, term=None, section_num=None):
        query="select * from class where course_code=%s"
        input_list=[course_code]
        
        if term:
            query=query+ "and term =%s"
            input_list.append(term)
            
            if section_num:
                query=query+ "and section_num =%s"
                input_list.append(section_num)
                
        res=read_query(self.con, query, tuple(input_list))
        
        if len(res)>1:
                print(f"There are Multiple classes for {course_code}. Please enter the term and section number!")
        elif len(res)==1:
            query="""update class
            set class_status=if(course_code=%s and term=%s and section_num=%s,1,0)"""
            execute_query(self.con,query,(course_code, term, section_num))
            print("Found!!!")
            print(f"{course_code}, {term}, section: {section_num} is active")
        else:
            print("Invalid entry. Enter correct details.")
        
    # display the current active class 
    def show_class(self):       
        query="""select * from class where class_status=1;
         """
        res=read_query(self.con, query)
        #print(res)
        if len(res)!=0:
            #df = pd.DataFrame(res, columns=['CLASS_ID', 'COURSE_CODE', 'TERM', 'SECTION_NUM', 'CLASS_DESC', 'CLASS_STATUS'])
            #pd.set_option('display.max_columns',None)
            #pd.set_option('display.max_rows',None)
            #print(df.to_string(index=False))
            for i in res:
                print(f"Active class: {i}")
            return res
        else:
            print(f"There are no active classes")
       
            
#cm=ClassManagement()

#cm.create_class('CS410','Fall23',1,'Databases')
#cm.create_class('CS410','Fall23',2,'Databases')    

#cm.list_class()   
#cm.select_class('CS410','Fall23')
#cm.show_class()
