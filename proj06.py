###########################################################
#  Computer Project #6
#
#  1. Yes the minorities make up heigher percentage of execution as compared 
#     to white because there are 273 minority people executed as compared to 
#     225 white poeple
#   
#  2. Minority killing white is 28 which is much heigher than white killing
#     minority which is just 7
#
#  3. There are no case for women killing men in the file where as there are
#     65 cases for men killing women
#  
#  4. Men make up a really high number of execution which is 118 cases where 
#     as there was only one woman who got executed
#
###########################################################
 

import csv

def open_file():#open file function
    """this funtion prompts to open a file till the user enters a file that is
    there in the folder"""
    while True:#infinite loop till the user enters correct file name
      try:  #try-except feature to account for errors
         file_name=input("Enter a file name: ")#input file name
         fp=open(file_name)#file open function using file object fp
         return fp#end of funtion
      except FileNotFoundError:#error case
          print("Error. Please try again")#displays error
          

def read_file():#read the file and extract relevant data
    """This funtion open the file through open_file funtion and then 
    create a list of tupple with the race, gender and the victim details and
    the list"""
    fp = open_file()   # open file as usual
    csv_fp = csv.reader(fp)  # invoke reader
    race_gender_victim_list=[]#initiates list
    race_gender_victim_tupple=()#initiates tupple
    for L in csv_fp:#goes through each line in the file
        race_gender_victim_tupple=(L[15].lower(),L[16].lower(),L[27].lower())\
#stores lower case race, gender , victim detail
        race_gender_victim_list.append(race_gender_victim_tupple)\
#adds tupple to the list
    race_gender_victim_list.pop(0)#removes the first element in the list
    fp.close()#closes the file
    return race_gender_victim_list#return the list

def male_vs_female(L):
    """This funtion takes a list of tupple with race, gender and victim details
    and them counts the number of male """
    N=0#the number of item that are relevant to this funtion
    male_count=0#the number of male in the list 
    female_count=0#the number of female in the list
    for item in L:#loop till the end of list
        if item[1]=='male':#if the entry is of male
            male_count+=1#increments the male count
            N+=1#increments the total entry considered
        elif item[1]=='female':#if the entry is of male
            female_count+=1#increments the female count
            N+=1#increments the count for total entries considered 
    return N,male_count,female_count\
#returns the total counts, male count and female count


def white_vs_minority(L):
    """This funtion takes a list of tupple with race, gender and victim details
    and them counts the number of black, hispanic and white people in 
    the list """
    hispanic_count=0
    black_count=0
    white_count=0  
    race_count=0
    for item in L:#loop till the end of list
        
        if item[0]=='white':#if the accused is a white person
            white_count+=1#increment the white count
        elif item[0]=='black':#if the accused is a black person
            black_count+=1#increment the black counts
        elif item[0]=='hispanic':#if the accused is hispanic person
            hispanic_count+=1#increments the hispanic count
        else: #in case the data is not available it continues the loop 
            continue#so that the entire race count is not affected
        race_count+=1#increments count for accused whose race is available
    return race_count,white_count,hispanic_count,black_count#returns the data

def race_difference(L):
    """This funtion takes a list of tupple with race, gender and victim details
    and them counts the attacks on white people by minority people, minority 
    by white people and female on male and male on female   """
   
    minority_on_white=0#initiatlizes minority on white crime count
    white_on_minority=0#initiatlizes white on  minority crime count
    female_on_male=0#initiatlizes female on male crime count
    male_on_female=0#initiatlizes male on female crime count
    N=0    #total case considered count
    for item in L:#loop till the end of list
        if 'not available' in item or '' in item:\
        #if the data field is empty or not available
            continue#does not execute the rest of the loop
        else:#if the data is available
            N+=1#increments the total case considered count
            if ('black' in item[0] or 'hispanic' in item[0]) and 'white' in \
item[2]:
                minority_on_white+=1#increment for minority on white crime case
                
            if ('black' in item[2] or 'hispanic' in item[2]) and 'white' in\
item[0]:
                white_on_minority+=1#increments white on minority crime case
                
            if 'female' in item[1] and ' male' in item[2]:
                female_on_male+=1#increments the female on male crime case
                  
            if 'male' == item[1] and 'female' in item[2]:
                male_on_female+=1#increments male on female crime case
    return N,minority_on_white,male_on_female,female_on_male,white_on_minority

rgv_list=read_file()#tupple of race, gender, victim details in a list

race_count,white_count,hispanic_count,black_count=white_vs_minority(rgv_list)\
#calls the white vs minority funtion and gets data
    
gender_count,male_count,female_count=male_vs_female(rgv_list)\
#calls male vs female funtion

difference_count,minority_on_white,male_on_female,female_on_male,\
white_on_minority=race_difference(rgv_list)#calls race difference function

print("="*40 )#print data separation line

print('White vs. Minority')#print header
print('N = {}'.format(race_count))#print the total race count
print('White: {}'.format(white_count))#print the white count
print('Black: {}'.format(black_count))#print the white count
print('hispanic: {}'.format(hispanic_count))#prints the hispanic count
print('Minority = Black + Hispanic: {}'.format(black_count+hispanic_count))\
#print the total minority count

print("="*40 )#print data separation line

print('Male vs. Female')#print the header 
print('N = {}'.format(gender_count))#print total gender count
print('Male: {}'.format(male_count))#print the total male count
print('Female: {}'.format(female_count))#print the total female count

print("="*40 )#print data separation line

print('Race difference between perpetrator and victim.')##prints the header 
print('N = {}'.format(difference_count))\
#print the total cases with race, gender and victim details available
print('Minority-on-white: {}'.format(minority_on_white))\
#print the minority on white crime cases
print('Male-on-female: {}'.format(male_on_female))\
#print male in female crime cases
print('Female-on-male: {}'.format(female_on_male))\
#print female on male crime cases
print('White-on-minority: {}'.format(white_on_minority))\
#print white on minority crime cases

    
    
# Questions
# Q1: 7
# Q2: 1
# Q3: 1
# Q4: 7
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

