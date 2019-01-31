###########################################################
#  Computer Project #11
#
#  Main application
#    Impost classes ,Student and class Grade
#    student has first name last name and grade
#    grade has proj name grade and weight of proj
#    student has add_grad which add the input grade
#    student has calculate grade which calculate all the grades
#    opoen student file and grades file
#    extract data
#    display each students grades in individual projects and exams
#           along with final grade
###########################################################

import classes

try:
    fp_student=open('students.txt')#open file
    fp_grades=open('grades.txt')
    
    
    student_list=[]
    first_name=[]
    last_name=[]
    
    for line in fp_student:#gets all the student file data
        x=line.strip().split()
        student_list.append(x)

    
    grades_list=[]
    for line in fp_grades:#gets all the grade file data
        
        x=line.strip().split()
        grades_list.append(x)
    grade_classlst=[]
    student_classlst=[]
    
    for item in student_list:#makes list of studetn object
        student_classlst.append(classes.Student(item[1],item[2],id=int(item[0])))
    
    
    for i in range(2,len(grades_list)):#adds all the data of grade of each studetn and add it to its relevent student object
        for j in range(1,len(grades_list[i])):
            try:#to manage index error
    
                grade_classlst.append(classes.Grade((grades_list[1][j]),float(grades_list[i][j]),float(grades_list[0][j])))           
    
                
            except:
                continue

        for n,k in enumerate(student_classlst):
            try:#to manage index error
                if int(grades_list[i][0])==int(k.id_int):
                    #print('Success')
                    student_classlst[n].add_grade(grade_classlst)
                    break
            except:
                continue
        grade_classlst=[]
            
    for item in student_classlst:#print the data collected 
        print(item)
        print('{:<13}:{:>6}%'.format('Final grade',int(item.calculate_grade())))
        print()

except:
    print('File not found')
    
