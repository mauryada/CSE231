    ###########################################################
    #  Computer Project #3
    #
    #  Tuition fees calculator
    #     Promt user for inputs (residence,level,college and credits) 
    #     calculate the tuition fees based on the information provided
    #     promts to enter college only if you are junior, senior or  graduate  
    #     displays error if incorrect details entered or a typo
    #     adds special fees in case of colleges
    #     adds appropriate taxes 
    #     displays the cost
    #     ask to start all over again
    ###########################################################
 
answer='yes'

while answer=='yes': #program goes on as long as user enters yes (not case sensitive)
     cost=0 #cost initiation eqauls zero
     resident=input("Resident (Yes/No):").lower()#inputs residence status coverts it into lower case
     level=input("Input level - Freshman, Sophomore, Junior, Senior, Graduate, None: ").lower()#inputs level
     if resident == 'yes':#case division starts from residence status 
        if level == 'freshman' or level == 'sophomore':#for freshman and sophomore
            credit=int(input("Input credit this semester: "))#input number or credit
            cost+=468.75*credit#cost for credits
            cost+=18 #ASMSU Tax
            cost+=3 #Radio Tax
        elif level == 'senior' or level == 'junior' :#case for senior or junior
            college=input("College - business, engineering, health, science, None: ").lower()#college input
            credit=int(input("Input credit this semester: "))#credit in integer
            if college =='none':#for those not in the college mentioned
                cost+=523.25*credit#cost of credits
                cost+=18 #ASMSU Tax
                cost+=3 #Radio Tax
            if credit<5:#special fees for part time jobs
                if college == 'business':#for business major
                    cost+=109.00#special business fees
                    cost+=523.25*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
                if college == 'engineering':
                    cost+=387.00#special engineering fees
                    cost+=523.25*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
                if college == 'health' or college == 'sciences' :
                    cost+=50.00#special health or sciences fees
                    cost+=523.25*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
            else :#special fees case for full time students
                if college == 'business':#business college case 
                    cost+=218.00#special business fees
                    cost+=523.25*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
                if college == 'engineering':#engineering case
                    cost+=645.00#special engineering fees
                    cost+=523.25*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
                if college == 'health' or college == 'sciences' :#health and science case
                    cost+=100.00#special heath or sciences fees
                    cost+=523.25*credit
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
            
        elif level =='graduate':#non resident graduate
            college=input("College - business, engineering, health, science, None: ").lower()#input college
            credit=int(input("Input credit this semester: "))#input credits
            if college =='business' or college=='health' or college=='science' or college=='none':#non engineering colleges
                    cost+=698.50*credit#credit
                    cost+=11 #COGS Tax
                    cost+=3 #Radio Tax
            if credit<5:#part time graduate students
               cost+=37.50#
               if college == 'engineering':#part time engineering students
                    cost+=387.00#engineering special fees part time graduate
                    cost+=698.50*credit#cost of credit
                    cost+=11 #COGS Tax
                    cost+=3 #Radio Tax
            else :#full time engineering 
                cost+=75.00#full time special fees
                if college == 'engineering':
                    cost+=645.00 #full time special engineering fees 
                    cost+=698.50*credit
                    cost+=11 #COGS Tax
                    cost+=3 #Radio Tax
            
     elif resident == 'no':#non resident case
         if level == 'freshman' or level == 'sophomore':#freshman and sophomore case
            credit=int(input("Input credit this semester: "))#credit input
            cost+=1263.00*credit#cost of credits
            cost+=18 #ASMSU Tax
            cost+=3#Radio tax
         elif level == 'senior' or level == 'junior' :#case for senior or junior
            college=input("College - business, engineering, health, sciences, None: ").lower()#college input
            credit=int(input("Input credit this semester: "))#credit in integer
            if college =='none':#for those not in the college mentioned
                cost+=1302.75*credit#cost of credits
                cost+=18 #ASMSU Tax
                cost+=3 #Radio Tax
            if credit<5:#special fees for part time jobs
                if college == 'business':#for business major
                    cost+=109.00#special business fees
                    cost+=1302.75*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
                if college == 'engineering':
                    cost+=387.00#special engineering fees
                    cost+=1302.75*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
                if college == 'health' or college == 'sciences' :
                    cost+=50.00#special health or sciences fees
                    cost+=1302.75*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
            else :#special fees case for full time students
                if college == 'business':#business college case 
                    cost+=218.00#special business fees
                    cost+=1302.75*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
                if college == 'engineering':#engineering case
                    cost+=645.00#special engineering fees
                    cost+=1302.75*credit#cost of credits
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
                if college == 'health' or college == 'sciences' :#health and science case
                    cost+=100.00#special heath or sciences fees
                    cost+=1302.75*credit#cost of credit
                    cost+=18 #ASMSU Tax
                    cost+=3 #Radio Tax
         elif level =='graduate':
            college=input("College - business, engineering, health, sciences, None: ").lower()#input college
            credit=int(input("Input credit this semester: "))#input credit
            if college =='business' or college=='heath' or college=='science' or college=='none':#
                    cost+=1372.00*credit#cost of credit
                    cost+=11 #COGS Tax
                    cost+=3 #Radio Tax
            if credit<5:#part time student
               cost+=37.50#special graduate fee
               if college == 'engineering':
                    cost+=387.00   #special engineering fees
                    cost+=1372.00*credit#cost of credit
                    cost+=11 #COGS Tax
                    cost+=3 #Radio Tax
            else :#full time student 
                cost+=75.00#special graduate fees
                if college == 'engineering':
                    cost+=645.00 #special engineeering fees
                    cost+=1372.00*credit#cost of credit
                    cost+=11 #COGS Tax
                    cost+=3 #Radio Tax
            
     if cost == 0:#if user makes a typo the program will not work and the cost is zero
         print("Error in input try again!")#outputs error
     else:
         if credit>5:#state news tax
             cost+=5#state news tax
         print("$"+'{:,.2f}'.format(cost))#prints cost with '$' and cents as decimal
          
     answer= input ("Do you want to calculate again (Yes/No):")#check if you want to repeat the calculation
     
     
     
# Questions
# Q1: 6
# Q2: 2
# Q3: 2
# Q4: 6