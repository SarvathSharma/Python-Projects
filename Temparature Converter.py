#######################################################
# Sarvath Sharma
# Computer Science 20
# March 16, 2017
# Credits: Caleb, Oguzhan and Xyre
# Temperature Conversion Program
# Purpose: To convert a temperature from celsius to fahrenheit.
#######################################################
foolprooftest = False
def c_to_f() :
    try:
        number_used = int(input("Please enter the number?"))
        answer = str(round((9*number_used) / 5 + 32))
        print (number_used, "degrees Celsius is equal to " + answer + " degrees Fahrenheit.")
    except ValueError:
        print ("Sorry, try again.")

def f_to_c() :
    try:
        number_given = int(input("Please enter the number?"))
        convert = str(round((number_given - 32) * 5/9))
        print (number_given, "degrees Fahrenheit is equal to " + convert + " degrees Celsius.")
    except ValueError:
        print ("Sorry, try again.")


#This part makes the code foolproof, so that it doesn't crash if you type something wrong
try:
    temp = input("Please enter 1 for Celcius or 2 for Fahrenheit")
    temp = int(temp)
    while foolprooftest == False:
        if temp > 2 or temp < 1:
                numbers = int(input("Invalid input. Please enter 1 for Celcius or 2 for Fahrenheit"))
                if numbers == 1:
                    c_to_f()
                    foolprooftest = True
                if numbers == 2:
                    f_to_c()
                    foolprooftest = True
        else:
                foolprooftest = True
                if temp == 1:
                    c_to_f()
                if temp == 2:
                    f_to_c()
except ValueError:
    print ("Please try again!!")