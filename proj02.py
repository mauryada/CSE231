    #######################################################
    #  Computer Project #2
    #
    #  Algorithm
    #    prompt for an integer
    #    input an integer
    #    display individual digits and there sum
    #######################################################
 

str_digit=input("Input an Integer ") #Inputs the number in a string
int_digit=int(str_digit)  #Converts the string into an integer
int_summ=0

while True:
    if int_digit<1:
        print("Enter a positive integer")
        str_digit=input("Input an Integer ") #Inputs the number in a string
        int_digit=int(str_digit)  #Converts the string into an integer
    else: 
        break

while int_digit>0:# The loop goes on till we have the last digit of the integer
                  # and also till the last digit of the the sum

   while int_digit>9: #This loop goes on the till the second last digit
                      #because otherwise it prints an extra '+' at the end

        int_summ+=int_digit%10 #Adds the sum of individual digit
        print(int_digit%10, "+ ", end='') #Print individual digit
        int_digit=int_digit//10 #Helps point to the next digit as the loop continues
    
   int_summ+=int_digit%10 #last iteration for the last digit reason explained above
   print(int_digit%10, "=", int_summ)
   int_digit=int_digit//10
   if int_summ>9: #if we have sum that is two digit or more we continue
           int_digit=int_summ #when we dont have a single digit sum it continues the process
           int_summ=0 #This continues to calculate the sum of the 2 digit or more integer sum
    