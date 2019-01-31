    ###########################################################
    #  Computer Project #4
    #
    #  Algorithm
    #       prompts to input file name 
    #       shows error if the file does not exist    
    #       finds specific data from the file
    #       displays the data in the specified format
    ###########################################################

def open_file():#open file function
    
    while True:#infinite loop till the user enters correct file name
      try:  #try-except feature to account for errors
         file_name=input("Enter a file name: ")#input file name
         fp=open(file_name)#file open function using file object fp
         return fp#end of funtion
      except FileNotFoundError:#error case
          print("Error. Please try again")#displays error
        
def find_min_percent(line):#minimum percentage finder in the GDP
    min_value = 10000000 # some large value to initiate comparison 
    value=0#initializes the value variable
    index=0#index counter
    while True:#infinite loop till the end of line
        try:#try-except feature to account for errors
            value=float(line9[76+12*index:76+12+12*index])#converts the slice of string into floating type variable
            if value < min_value:#finds the smallest number in the line 
                min_value = value#stores the smallest number
                min_index=index#stores the index of the smallest number
            index+=1#points to the next index
            
        except ValueError:#error that occurs at the end of line 
            break#breaks the loop when error occurs
    return min_value,min_index#returns the values
    
def find_max_percent(line):#minimum percentage finder in the GDP
    max_value = -10000000 # some small value to initiate comparison
    value=0#initiates the values variable
    index=0#index counter
    while True:#infinite loop till the end of line
        try:#try-except feature to account for errors 
            value=float(line9[76+12*index:76+12+12*index])#converts the slice of string into floating type variable 
            if value > max_value: #finds the largest number in the line 
                max_value = value#stores the largest value
                max_index=index#stores the index of the largest value
            index+=1#points to the next index
            
        except ValueError:#error that occurs at the end of line 
            break#breaks the loop when error occurs
    return max_value,max_index#return the value

def find_gdp(line,index):#finds the value of the gdp
    gdp_val=float(line[76+12*index:76+12+12*index])#converts the slice of string into floating type variable
    return gdp_val#returns the gdp
    
def find_year(line,index):#finds the year of the index passed as an argument 
    year_val=int(line[76+12*index:76+12+12*index])#converts the string into int type
    return year_val#returns the value

def display(min_val, min_year, min_val_gdp, max_val,max_year,max_val_gdp):#display the result of the program
    print("\nGross Domestic Product \n")#prints the introduction 
    print('The minimum change in GDP was {} in {} when the GDP was {:,.2f} trillion dollars'.format(min_val,min_year,min_val_gdp/1000))#prints the change in GDP the year and value of lowest case
    print('The maximum change in GDP was {} in {} when the GDP was {:,.2f} trillion dollars'.format(max_val,max_year,max_val_gdp/1000))#prints the change in GDP the year and value of highest case

 
file_object=open_file()#Calls the open file function created above
count=0#counts the line
for line in file_object:#loop extracts each line in the file 
    count+=1#increments counts
    if count ==8:#checks if we reach line 8
        line8 = line#stores line 8
    elif count == 9:#check if we reach line 9 
        line9 = line#stores line 9
    elif count == 44:#check if we reach line 44
        line44= line#stores line 44

min_val,min_index= find_min_percent(line9)#finds min percentage value and its index
max_val,max_index= find_max_percent(line9)#finds max percentage value and its index

min_val_gdp=find_gdp(line44,min_index)#finds min value of the gdp
max_val_gdp=find_gdp(line44,max_index)#finds max value of the gdp

min_year=find_year(line8,min_index)#finds the year of the min gdp using the index
max_year=find_year(line8,max_index)#finds the year of the max gdp using the index

display(min_val, min_year, min_val_gdp, max_val,max_year,max_val_gdp)#DISPLAYS THE FINAL OUTPUT

# Questions
# Q1: 7
# Q2: 2
# Q3: 2
# Q4: 7