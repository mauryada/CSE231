
    ###########################################################
    #  Computer Project #5
    #
    #  Algorithm
    #    Opens a file with data on RedCedarRiver
    #    read file and extract relevant data (Year, Month and Flow)
    #    Plots the graph with the average flow of EACH year VS. year
    #    Display Annual average flow
    #       output the number of digits
    #       prompt for an integer
    #       input an integer
    #    display closing message
    ###########################################################
 

import pylab#import pylab

def open_file():#open file function
    
    while True:#infinite loop till the user enters correct file name
      try:  #try-except feature to account for errors
         file_name=input("Input a file name: ")#input file name
         fp=open(file_name)#file open function using file object fp
         return fp#end of funtion
      except FileNotFoundError:#error case
          print("Error. Please try again")#displays error
        
def draw_plot( x, y, plt_title, x_label, y_label):#takes the arguments to create a graph
    ''' Draw x vs. y (lists should have the same length)
    Sets the title of plot and the labels of x and y axis '''
    
    pylab.title(plt_title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    
    pylab.plot( x, y )
    pylab.show()
    
def read_file():#read the file and extract relevant data
    fp=open_file()    #file pointer to point to the file opened by open_file funtion
    tuple_list=[]#initiates tuple_list
    for line in fp:#read each line in fp
        my_tuple = (int(line[26:31]),int(line[31:33]),float(line[33:]))#creats a tuple with year month and flow
        tuple_list.append(my_tuple)#adds the tupple to the list
        
    return tuple_list


def annual_average(L):#put the average of each year in a list of tuples with year and there average
    annual_average=0#initiates annual average
    annual_average_list=[]#initiates the list
    for item in L:#for each tuple in list
        if item[1]<12:#adds the flow of the month 1-11 
            annual_average+=item[2]#into annual_average
        else:#for the month 12
            annual_average+=item[2]#add the flow of 12th month into annual_average
            annual_average=annual_average/12#calcute the 'Mean'
            annual_average_tupple=(item[0],annual_average)#creats a tuple with years and annual_average
            annual_average_list.append(annual_average_tupple)#adds the tupple to a list of annual averages
            annual_average=0#reinitiates the average equal to zero
    return annual_average_list#return the list of tuple with years and there annual average


def month_average(L,M):#argument List as L and month as M
    month_list=[]#list with months

    for x in range(M-1,len(L),12):#i am using 'for' loop instead of 'for each', 
                                  #the loop starts from the month and goes till the end of L with increment of 12 (12 months) 
        month_list+=[(L[x][0],L[x][2])]#L[x] is the tupple at the index x
    return month_list#returns the list
        
def get_month():#get input month from user in range of 1-12 find its corresponding name and return it as tuple
    while True:#loop till the user enters correct value
        try:    #try/except if the user enter anything other than integer
            month=input("Enter a month (1-12): ")#input the number as a string
            month=int(month)#converts it into int
            if month not in range (1,13):#checks if it is in the range of 1-12
                print('Error. Integer out of range.')#if not in range prints the error
                continue#ask for the input again
            else:#if the input is in range of 1-12
                break#break the loop
        except ValueError:#if input is not integer
            print('Error. Not an integer')#print the error
    months=[(1,'January'),(2,'Febuary'),(3,'March'),(4,'April'),(5,'May')]#database for the month with their name
    months+=[(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October')]
    months+=[(11,'November'),(12,'December')]
    for x in months:#finds the user input month in our data
        if month==x[0]:#checks if we found the input
            return x#return the tuple with month integer and its name in string



relevant_list=read_file()#open the file and read it to extract relevent list to a variable list

annual_average=annual_average(relevant_list)#extract annual average from the relevant list

years_list=[]#initiates years list
flow_list=[]#initiates the flow list
for item in annual_average:#for each item in annual average list
    years_list+=[item[0]]#stores a list of years in the file
    flow_list+=[item[1]]#and the average annual flow of the corresponding year
    
    
draw_plot(years_list,flow_list ,'annual average flow 1932-2015','year','flow')#draws the graph

print('Annual Average Flow')#print the title for the annual average flow
print('Years         Flow')#print row title
for item in annual_average:#extract each item from annual_average
    print ('{}{:>14,.2f}'.format(item[0],item[1]))#print years and flow in there respective row


month_int,month_str=get_month()#input the month in integer and stores its value as integer and its name as string.
month_flow_list=month_average(relevant_list,month_int)#extracts data for the user input month

month_flow=[]#initiates the month flow list
for item in month_flow_list:#for each item in month flow list
    month_flow+=[item[1]]#stores a list of flow of each month over the years
    
draw_plot(years_list,month_flow ,'Average Flow for {}'.format(month_str),'year','flow')

print('Annual Flow for {}'.format(month_str))#print the title for the month input by the user
print('Years         Flow')#print row title

for item in month_flow_list:#extract each item from month flow list
    print ('{}{:>14,.2f}'.format(item[0],item[1]))#print years and flow in their respective row



# Questions
# Q1: 7
# Q2: 1
# Q3: 2
# Q4: 7





