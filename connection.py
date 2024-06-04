# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:26:01 2023

@author: thari
"""

import mysql.connector as connector
from mysql.connector import Error
import pandas as pd

#connection
def create_server_connection(host_name, user_name, user_password):
    con=None
    try:
        con=connector.connect(host=host_name,
                              user=user_name,
                              password=user_password)
        #print("Mysql database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return con

pw="@@Doodle1243"
db = "school_mgmt"

con = create_server_connection("127.0.0.1", "root", pw)

# create a new database school_mgmt
def create_database(con,query):
    cursor=con.cursor()
    try:
        cursor.execute(query)
        #print("Databse created successfully!")
    except Error as err:
        print(f"Error:'{err}'")
create_database_query="create database if not exists school_mgmt"
create_database(con,create_database_query)

# connect database
#db = "school_mgmt"
def create_db_connection(host_name, user_name, user_pw, db_name):
    con=None
    try:
        con=connector.connect(host=host_name,
                              user=user_name,
                              password=user_pw,
                              database=db_name)
        #print("Mysql database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return con

# Function to execute queries
def execute_query(con,query,args=None):
    cursor=con.cursor()
    try:
        if args:
            cursor.execute(query,args)
            con.commit()
            #print("Query was successful!")
        else:
            cursor.execute(query)
            con.commit()
            #print("Query was successful!")
    except Error as err:
        print(f"Error:'{err}'")


# To read the query and display the connection
def read_query(con, query, args=None):
    cursor=con.cursor();
    result=None
    try:
        if args:
            cursor.execute(query,args)
            result=cursor.fetchall()
            return result
        else:
            cursor.execute(query)
            result=cursor.fetchall()
            return result
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()
    return result