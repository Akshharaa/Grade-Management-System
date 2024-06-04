# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:58:53 2023

@author: thari
"""

from ClassManagement import ClassManagement
from CategoryManagement import CategoryManagement
from StudentManagement import StudentManagement
from GradeReporting import GradeReporting

def main():
    while True:
        print()
        print("********************WELCOME TO SCHOOL MANAGEMENT SYSTEM***************************")       
        print()
        print("1. CLASS MANAGEMENT")
        print("2. CATEGORY MANAGEMENT")
        print("3. STUDENT MANAGEMENT")
        print("4. GRADE REPORTING")
        print("5. EXIT")
        print()
        
        try:
            choice=int(input())
            if(choice==1):
                cm=ClassManagement()
                while True:                   
                    print()
                    print("CLASS MANAGEMENT")
                    print()
                    print("Select an option:")
                    print("1. create class")
                    print("2. list class")
                    print("3. activate a class")
                    print("4. list active class")
                    print("5. exit")
                    print()
                    
                    try:
                        choice=int(input())
                        if(choice==1):
                            #create class
                            print()
                            course_code=input("Enter course code: ")
                            term=input("Enter course term: ")
                            section_num=int(input("Enter the section number: "))
                            class_desc=input("Enter course course description: ")               
                            cm.create_class(course_code, term, section_num, class_desc)
                            pass
                        elif choice==2:
                            #list class
                            print()
                            cm.list_class()
                            pass
                        elif choice==3:
                            #activate a class
                            course_code=input("Enter course number: ")
                            term=input("Enter term(optional): ")
                            section_number=input("Enter section number(optional): ")
                            cm.select_class(course_code, term, section_number)
                            pass
                        elif choice==4:
                            #show active class
                            print()
                            cm.show_class()
                            pass
                        elif choice==5:
                            break
                        else:
                            print("Invalid input! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details Entered! Try again")               
                pass
            elif choice==2:
                cm=ClassManagement()
                cat_mgmt=CategoryManagement(cm)
                while True:
                    print()
                    print("CATEGORY MANAGEMENT")
                    print()
                    print("Select an option:")
                    print("1. show categories")
                    print("2. add categories")
                    print("3. show assignmetns")
                    print("4. add assignments")
                    print("5. exit")
                    print()
                    
                    try:
                        choice=int(input())
                        if(choice==1):
                            #show categories
                            print()
                            cat_mgmt.show_categories()
                            pass
                        elif choice==2:
                            #add categories
                            print()
                            category_name=input("Enter category name: ")
                            weight=float(input("Enter the weight: "))
                            cat_mgmt.add_categories(category_name,weight)
                            pass
                        elif choice==3:
                            print()
                            #show assignments
                            cat_mgmt.show_assignments()   
                            #print()
                            pass
                        elif choice==4:
                            #add assignments
                            print()
                            assignment_name=input("Enter assignment name: ")
                            category_name=input("Enter category name: ")
                            assignment_desc=input("Enter assignment description: ")                 
                            points=int(input("Enter the points: "))                           
                            print()
                            cat_mgmt.add_assignments(assignment_name, category_name, assignment_desc, points)
                            pass
                        elif choice==5:
                            break
                        else:
                            print("Invalid input! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details Entered! Try again")  
                
                pass
            elif choice==3:
                cm=ClassManagement()
                sm=StudentManagement(cm)
                while True:
                    print()
                    print("STUDENT MANAGEMENT")
                    print()
                    print("Select an option:")
                    print("1. add and enroll a new student")
                    print("2. enroll an existing student")
                    print("3. list all students in current class")
                    print("4. list of students with the given string")
                    print("5. grades")
                    print("6. exit")
                    print()
                    
                    try:
                        choice=int(input())
                        if(choice==1):
                            #add and enroll a new student
                           print()
                           username=input("Enter username: ")
                           student_id=int(input("Enter student_id: "))
                           first=input("Enter first name: ")                 
                           last=input("Enter last name: ")                            
                           print()
                           sm.add_student(username, student_id, first, last)
                           pass
                        elif choice==2:
                            #enroll an existing student
                            print()
                            username=input("Enter username: ")
                            print()
                            sm.add_student1(username)
                            pass
                        elif choice==3:
                            #list of students in class
                            print()   
                            sm.show_students()
                            #print()
                            pass
                        elif choice==4:  
                            print()
                            string=input("Enter the string: ")                           
                            print()
                            sm.show_students1(string)
                            pass
                        elif choice==5:
                            #grades
                            print()
                            assignment_name=input("Enter assignment name: ")
                            username=input("Enter username: ")
                            grade=int(input("Enter grade: "))
                            print()
                            sm.grades(assignment_name, username, grade)
                            pass
                        elif choice==6:
                            break
                        else:
                            print("Invalid input! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details Entered! Try again")  
                
                pass
            elif choice==4:
                cm=ClassManagement()
                gr=GradeReporting(cm)
                while True:
                    print()
                    print("GRADE REPORTING")
                    print()
                    print("Select an option:")
                    print("1. student's current grade")
                    print("2. gradebook")
                    print("3. exit")
                    print()
                    
                    try:
                        choice=int(input())
                        if(choice==1):
                            #student's current grade
                           print()
                           username=input("Enter username: ")
                           print()
                           gr.student_grades(username)
                           pass
                        elif choice==2:
                            #gradebook  
                            print()
                            gr.gradebook()
                            pass
                        elif choice==3:
                            break
                        else:
                            print("Invalid input! Try again")
                    except Exception as e:
                        print(e)
                        print("Invalid Details Entered! Try again")  
                
                pass
            elif choice==5:
                break
        except Exception as e:
            print(e)
            print("Invalid Details Entered! Try again")
    
            
if __name__ =="__main__":
    main()