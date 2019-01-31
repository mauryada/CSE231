###########################################################
#  Computer Project #9
#
#  This program promts to open a file
#  prompts to enter a string
#  finds the string prefix in the dictonary
#  display all the words which complete the prefix string entered
#  stops the program when '#' is entered
###########################################################
 


import string

def open_file():#open file function
    """this funtion prompts to open a file till the user enters a file that is
    there in the folder"""
    while True:#infinite loop till the user enters correct file name
      try:  #try-except feature to account for errors
         file_name=input("Input a file name: ")#input file name
         fp=open(file_name)#file open function using file object fp
         return fp#end of funtion
      except FileNotFoundError:#error case
          print("Error. Please try again")#displays error
          


def fill_completions(fd):

    '''This function takes a file pointer as an argument and return a dictionary
    with tuples as key and a set of strings as argument'''
  



    line_list=[]#initialize line_list
    for line in fd:#takes a line from file pointer
        line_list+=line.split()  #makes a list of word with splitting at ' '
        
      
    word_set=set()#initializes set
    for item in line_list:#for each item in line list
        
        item=item.strip(string.punctuation)#removes punctuation from the end
        word_set.add(item)#add the item to set
    
    
    c_dict={}#initialize dictionary
    
    for word in word_set:#for each word in word set
        word=word.lower()#makes the word in lower case
        break_statement=False#break statement for ignoring the cases 
        if len(word)==1:#if single character word
            break_statement=True#ignore single chacter word
    
        for char in string.punctuation:#it finds punctuation in word
            if char in word:#if punctuation found
                break_statement=True#break statement when 
                
            
        if break_statement:#break the statement true in case of this word
            continue
        for new_tuple in enumerate(word):#tuple has char and index as value
    
            if new_tuple in c_dict.keys():#if tuple key in dictionry
                c_dict[new_tuple].add(word)#add mores values to that key
            else:
                c_dict[new_tuple]={word}#create a key with values

    return c_dict           
    
def find_completions(prefix, c_dict):
    '''This funtion takes a dictionary and a string as argument and returns a set
    of words as which complete the incomplete string'''
    
    c_set=set()#initiates set
    try:
        c_set=c_dict[(0,prefix[0])]#first value of set
    except:#if first value is not in the dictionary
        None#does not crash the program
    
    for char_tuple in enumerate(prefix):#creates a tuple with index and character as value
        if char_tuple in c_dict:#if the tuple is key in c_dict
            c_set= c_set & c_dict[char_tuple]#adds the value to a set
    
    return c_set
    

    

def display(c_set):
    '''this function takes a set as argument and prints all the corresponding value
    also displays error if the set is empty'''
    if c_set == set():    
        print('Prefix not in the dictionary')
    else:
        for item in c_set:
            print(item, end=' ')
    print()

fp = open_file()#file pointer

c_dict=fill_completions(fp)

prefix =''

    
while True :#infinite loop
    
    prefix=input("Enter the prefix to complete (or '#' to quit): ")#takes a prefix of the word to find
    if prefix=='#':# if user wants to end
        break#break the loop
    prefix=prefix.lower()#makes the prefix to lower case
    
    c_set=find_completions(prefix,c_dict)#gets a set of common word with same prefix
    
    print("completion of {}: ".format(prefix), end = '') #prints the information
    display(c_set)#calls display


fp.close()#closes file


# Questions
# Q1: 7
# Q2: 1
# Q3: 1
# Q4: 7