    ###########################################################
    #  Computer Project #1
    #
    #  This program is to calculate wind chill temprature
    #       It takes input that is Temprature in Fahrenheit
    #       and wind speed in MPH and uses an equation
    #       to calclutate Wind Chill Temprature
    ###########################################################
import math
temprature_str = input('Please enter the temprature in Fahrenheit: ')
temprature_int = int(temprature_str)

windspeed_str = input('Please enter wind speed in MPH: ')
windspeed_float = float(windspeed_str)

WCT=35.74 + 0.6215*temprature_int - 35.75*(math.pow(windspeed_float,0.16))+0.4275*temprature_int*(math.pow(windspeed_float,0.16))

print ("The Wind Chill Temprature is:" , WCT)