###########################################################
#  Computer Project #7
#
#       Prompt the user for an input to enter decades,
#       if more than one enter, user seperate by comma ','
#       
#       print a graph with annual average city mileage of each 
#       manufacturer
#       
#       print a graph with annual average city mileage of each 
#       manufacturer
#       
#       Prints a table of entire average mileage over the period user 
#       enters in decade and the available information
#  
###########################################################

import csv
import pylab
import matplotlib.patches as patches

def open_file():#open file function
    """this funtion prompts to open a file till the user enters a file that is
    there in the folder"""
    decade_list=('1980','1990','2000','2010')   #list of decades of file
    decade_list_input=[]#initialize the input string variable
    fp_list=[]#file pointer list
    x=True#loop initializer and controller
    while x==True:#infinite loop till the user enters correct file name
      try:  #try-except feature to account for errors
         decade_list_input=input("Input multiple decades separated by commas, e.g. 1980, 1990, 2000: ")#input file name
         input_data=decade_list_input #to return the input given by the user 
         decade_list_input=decade_list_input.split(',')#split the string into list at the comma seperation
         for item in decade_list_input:#for each item in the list seperated by comma given by the user 
             item=item.strip()#removes the spaces from the end point of the item ie the single decade input
             if item in decade_list:#if the item is in decade list 
                item+='s.csv'#add the remainging characters to the file name and its extension
                
                fp=(open(item))#open the fiel
                
                fp_list.append(fp)#adds the file pointer into the list of file pointers
                x=False#controlls the loop, Stop the loop
             else:#if the user input decade is not in the available decade
                print('Error in decade') #display error
                x=True#continue the loop
                for item in fp_list:#go through  all previously opened files
                    item.close()#close all of the file that opened
                
      except FileNotFoundError:#error case
          print("file not found")#displays error
          x=True#continues the loop
          for item in fp_list:#go through  all previously opened files
              item.close()#close all of the file that opened
      
    return fp_list,input_data#return the list of pointers and the input string given by the user   

def plot_mileage(years,city,highway):
    '''Plot the city and highway mileage data.
       Input: years, a list of years;
              city, a dictionary with manufacturer as key and list of annual mileage as value;
              highway, a similar dictionary with a list of highway mileage as values.
       Requirement: all lists must be the same length.'''
    pylab.figure(1)
    pylab.plot(years, city['Ford'], 'r-', years, city['GM'], 'b-', years,
             city['Honda'], 'g-', years, city['Toyota'], 'y-')
    red_patch = patches.Patch(color='red', label='Ford')
    blue_patch = patches.Patch(color='blue', label='GM')
    green_patch = patches.Patch(color='green', label='Honda')
    yellow_patch = patches.Patch(color='yellow', label='Toyota')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('City Fuel Economy (MPG)')
    pylab.show()
    
    # Plot the highway mileage data.
    pylab.figure(2)
    pylab.plot(years, highway['Ford'], 'r-', years, highway['GM'], 'b-', years,
             highway['Honda'], 'g-', years, highway['Toyota'], 'y-')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('Highway Fuel Economy (MPG)')
    pylab.show()
    
def read_file(input_file):
    '''open the file pointer in csv reader ignores value from year 2017 gets teh
    manufacturer year and city milage and highway mileage fromt the file 
    makes a dictionary of manufacturers that has a dictionary of years that contain
    list of list that has city mileage list and highway mileage list also returns a 
    year range of the file '''
    
    dict_file={}#initialize the dictionary to contain the data of the file
    year_list=[]#the list of years whose data is availabel the file
    
    csv_input_file=csv.reader(input_file)#starts the file pointer in csv mode
    
    for L in csv_input_file:#for each row in the file
        manufacturer=L[46]#stores the value of the manufacturer
        year=L[63]#the year
      
        if year == '2017':#since the data from the year 2017 is incomplete we ignore entries of year 2017
            continue#prevents the loop to execute any further code in the loop and starts again
        if manufacturer in 'Chevrolet Pontiac Buick GMC Cadillac Oldsmobile Saturn':#All GM brands
            manufacturer = 'GM'#makes the manufacturer GM
        elif manufacturer in 'Ford Mercury Lincoln':#for all ford brands 
            manufacturer = 'Ford'#makes the manufacturer Ford
        elif manufacturer in 'Honda + Acura':#fot all the Honda brand
            manufacturer = 'Honda'#makes the manufacturer Honda
        elif manufacturer in 'Toyota Lexus Scion':#for all the toyota brand 
            manufacturer = 'Toyota'#makes the manufacturer Toyota
        else:#if any other manufacturer's car is encountered 
            continue#start the loop again with the next value
        year=int(year)#convert integer string year into integer
        city_mileage=int(L[4])#the city mileage as integer
        highway_mileage=int(L[34])#and the highway mileage as integer
        
        if year not in year_list:#if the year is not already in the year list 
            year_list.append(year)#add the year into the list of years 
            
        if  manufacturer not in dict_file:#is manufacturer is not in dictionary data file
            dict_file[manufacturer] = {year:[[city_mileage],[highway_mileage]]}#add the key 'Manufacturer' with its corresponding valaues
            
        else:#if the dictionary already has manufacturer is already in the dictionary
            
            if year not in dict_file[manufacturer]:#and the year is not in the dictionary 
               dict_file[manufacturer][year]=[[city_mileage],[highway_mileage]]#add the value for that correspoding manufacturer and year into the dictionary file
               continue#start the loop again and skip the next steps
               
            dict_file[manufacturer][year][0].append(city_mileage)#if the dictionary already has manufacturer is already in the dictionary
            dict_file[manufacturer][year][1].append(highway_mileage)#add city mileage to the 0 index and highway mileage to the 1st index
    input_file.close() #close all open file
    return dict_file, year_list#return the data file dictionary will all the files

def merge_dict(target,source):
    '''gets a list that contain data from a recently opended file adds that data into
    a dictioinary that contain data from previously opened file and returns the updated
   dictionary '''
    for manufacturer in source:#takes each manufacturer in the source
        if manufacturer in target:#if the manufacturer is already in the target
            target[manufacturer].update(source[manufacturer])#update its value in target with the values in the source
        else:#if not the manufacturer is not in the target already
            target[manufacturer] = source[manufacturer]#adds the manufacturer from source to target
    return target#return the dictionary target with all the values from source added
    
def average(target):
    '''gets a dictionary of data from all the files seperates them into into city 
    and highway averages for each year of each company'''
    year_city_list=[]#list of mileage values for each city at a single year
    year_highway_list=[]#list of mileage values for each highway at a single year
    
    target_average_city={}#the average city mileage for each year in a dictionary 
    target_average_highway={}#the average highwyay mileage for each year in a dictionary 
    
    average_city_list=[]#average city mileage list
    average_highway_list=[]#average highway mileage list 
    
    for manufacturer in target:#for each manufacturer in the target dictionary 
        average_city_list=[]#initializes the average city list and them re-initializes for the next manufacturer and so on
        average_highway_list=[]#initializes the average highway list and them re-initializes for the next manufacturer and so on
        
    
        for years in target[manufacturer]:#for each year value in the dictionary 'manufacturer' of dictionary 'Target'
            year_city_list=target[manufacturer][years][0]#takes the value of mileage of city in a particular year for a particular manufacturer
            year_highway_list=target[manufacturer][years][1]#takes the value of mileage of city in a particular year for a particular manufacturer 
            
            average_city_list.append(sum(year_city_list)/len(year_city_list))#Finds the average of the city mileage over the course of a year for a particular manufacturer and add this value to the average city list
            average_highway_list.append(sum(year_highway_list)/len(year_highway_list))#finds the average of the highway mileage over the course of a year for a particular manufacturer and this value to the average highway list
            
            ### end of loop with all the average of per year mileage in average city and highway list
            
        if manufacturer in target_average_city:#if the manufacturer we are working of is already in the total average city(if the value is not in target average city it wont be in target average highway)
            target_average_city[manufacturer].update(average_city_list)#updates the average city list to the manufacturer 
            target_average_highway[manufacturer].update(average_highway_list)#updates the average highway list to the manufacturer
        else:#if the manucaturer is not in the target_average_city (which in turn means not in target_average_highway)
            target_average_city[manufacturer]=average_city_list#adds the value of average city to the manufacturer key of the target city average dictionary 
            target_average_highway[manufacturer]=average_highway_list#adds the value of average highway to the manufacturer key of the target highway average dictionary
      #end of loop with target average city and target average highway
    return target_average_city, target_average_highway#returns the values

def display(city, highway,input_data):
    '''prints the table to display the average of mileage of each manufacturer over
    the entire period of decades that is input my the user'''
    
    print("Manufactures' average for {} \n City".format(input_data))#print the title for the table
    print('{:>20s}: {:<20s}'.format('Company','Mileage'))#print the column title
    for manufacturer in city:#for each manufacturer in the city  average dictonary
        print('{:>20s}: {:<.2f}'.format(manufacturer,sum(city[manufacturer])/len(city[manufacturer])))#print the average of the entire city milages 
    print('highway')#print highway case
    for manufacturer in highway:#for each manufacturer in the highway average dictionry 
        print('{:>20s}: {:<.2f}'.format(manufacturer,sum(highway[manufacturer])/len(highway[manufacturer])))#print the average of the entire highway milages 

fp_list,input_data=open_file()#calls the open_file function

target={}#initialize target dictionary
year_list=[]#initializes year_list

for item in fp_list:#for each file pointer in file pointer list
    source,years=read_file(item)#gets the source dictionary and years range of the opened file
    year_list+=years#years from the current file added to the final year list
    merge_dict(target,source)#add all the value od source to target and start all over agian

city,highway=average(target)#gets the city and highway values of from target

year_list.sort()#year list sorted 

plot_mileage(year_list,city,highway)#plot the value on graph

display(city,highway,input_data)#display the table
        
        
        
        
        