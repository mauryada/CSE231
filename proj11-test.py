###########################################################
#  Computer Project #11
#
#  TEST application
#    Test all the functions of classes
#    
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



# This is a sample proj11-test.py program
# There are two requirements:
#   A) Demonstrate all methods (except __repr__ which can only be demonstrated in the Python shell)
#   B) Include print statements so your output can be read and understood without reading the code

import classes

print("Create a Grade instance: p01, 75, .8")
g1 = classes.Grade("p01",75,.8)    # tests __init__
print("Print the Grade instance")
print(g1)        # tests __str__
# we cannot test __repr__ in a program, only in the Python shell

# Create another grade instance, let's call it g2
g2=classes.Grade('e01',74,0.7)
g3=classes.Grade('p02',90,0.2)

# Maybe create more grades
# Create a Student instance, let's call it s1
s1=classes.Student('carl','smith',id=7)

# Then print s1, include descriptive print statements such as above
# Demonstrate add_grade and calculate_grade
s1.add_grade(g1)
print(s1)
# Create another student instance, let's call it s2
s2=classes.Student('pablo','escobar',g1,id=9)

# Demonstrate comparison operators 
print()
print("After adding score of p01 to both pablo and Carl's score")
print()

print("Is Carl's score more than pablos? ",s1.__gt__(s2))
print("Is Carl's score less than pablos? ",s1.__lt__(s2))
print("Is Carl's score equal to than pablos? ",s1.__eq__(s2))

s2.add_grade(g3)
print()
print('After adding score of p02 to pablos')
print()
print("Is Carl's score more than pablos? ",s1.__gt__(s2))
print("Is Carl's score less than pablos? ",s1.__lt__(s2))
print("Is Carl's score equal to than pablos? ",s1.__eq__(s2))

s1.add_grade(g2)

print()
print('After adding score of e01 to carl')
print()
print("Is Carl's score more than pablos? ",s1.__gt__(s2))
print("Is Carl's score less than pablos? ",s1.__lt__(s2))
print("Is Carl's score equal to than pablos? ",s1.__eq__(s2))

