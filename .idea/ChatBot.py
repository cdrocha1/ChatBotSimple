

def filePrompt():
    fileP = input("User or File chat? (Enter User or File defualt is User)\n")  #determines if code will prompt or read off file
    if fileP.lower() == "file":
        user = False            #user boolean determines if program will prompt user
    else:
        user = True
    return user


def genderDecider():            #takes gender input and forms adequate response
    print("Hello, are you male or female?")
    if user == True:
        gender = input
    else:
        gender = content[0]
        print(gender)

    if gender.lower() == 'male':           #in the case the user enters capitalized variables
        print("Me too. ", end = '')
    elif gender.lower() == 'female':
        print("How excellent! ", end = '')
    else:
        print("I haven't heard of that but it sounds cool! ")

def majorDecider():
    print("Are  you a CS major?")
    if user == True:
        major = input
    else:
        major = content[1]
        print(major)
    if major.lower() == 'yes':
        print("Excellent, I am too.")

    if major.lower() == 'no':
        print("Too bad.")

def animalDetector():
    print("Anyway, whats an animal you like and two you don't?")
    if user == True:
        animal = input
    else:
        animal = content[2]
        print(animal)
    animal = animal.split(' ')
    print(animal[0], "awesome, but I hate", animal[-1], "too. Bye for now")


if __name__ == "__main__":
    user = filePrompt()
    if(user == False):
        file = input("name of the file: \n")
        myFile = open(file)
        content = myFile.read()     #reads file and splits by line
        content = content.splitlines()

    genderDecider()
    majorDecider()
    animalDetector()