
#User name & password for all three users
userNameOne = "sami"
passwordOne = "compsci"

userNameTwo = "shae"
passwordTwo = "binary"

userNameThree = "rak"
passwordThree = "helloWorld"

correctCredentialsEntered = False


#checking if input mathces id & password
def checkInput(user, password):
    '''Checks username and password if they are right for userOne.
    user --> str
    password --> str
    '''
    #checking if user and password are correct
    if user == userNameOne and password == passwordOne:
        print("It's great to see you")
        global correctCredentialsEntered
        correctCredentialsEntered = True

    #Checking if user is correct and password is wrong!
    elif user == userNameOne and password != passwordOne:
        print("Wrong password" +' '+ userNameOne)
    #Else check if it is other user
    else:
        checkInputTwo(user, password)

#checking if input matches userTwo id & pasword
def checkInputTwo(user, passwrod):
    '''Checks username and password if they are right for userTwo.
    user --> str
    password --> str
    '''
    #checking if user and password are correct
    if user == userNameTwo and password == passwordTwo:
        print("There are 10 types of people in the World..")
        global correctCredentialsEntered
        correctCredentialsEntered = True

    #Checking if user is correct and password is wrong!
    elif user == userNameTwo and password != passwordTwo:
        print("Wrong password" +' '+ userNameTwo)
    #Else check if it is other user
    else:
        checkInputThree(user, password)

#Checking if input mathces userThree id & password
def checkInputThree(user, password):
    '''Checks username and password if they are right for userThree.
    user --> str
    password --> str
    '''
    #checking if user and password are correct
    if user == userNameThree and password == passwordThree:
        print("Hey there rak")
        global correctCredentialsEntered
        correctCredentialsEntered = True

    #Checking if user is correct and password is wrong!
    elif user == userNameThree and password != passwordThree:
        print("Wrong password" +' ' + userNameThree)
    #Else print 'try again' if user name & password do not equal to any of the user's
    else:
        print("Try again!")

#Starting amount of attemps
attemps = 0

    #Setting limit for attemps!
while attemps < 4:
    if correctCredentialsEntered == False:
        userInput = input("Please enter your userName:")
        password = input("Please enter password:")
    #checking if input is right or wrong
        checkInput(userInput, password)
        attemps = attemps + 1
    else:
        attemps = 4

#printing go away after 4 attemps have occured



