# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task
print("hello from day3")

########################################################################
# Task 1:
# myName = input("WHat is your name?")
# myTitle = input("What is your title")
# myCommand = input("What is your command")
# print(myTitle + myName + " commands the troops to " + myCommand)

########################################################################
# Task 2:
name = "Javen "
num_pens = 10 
print(name + "bought " + str(num_pens) + " pens.")
########################################################################
# Task 3:
# num1 = int(input("Your first number is?"))
# num2 = int(input("Your second number is?"))
# sum = num1 + num2
# print(str(num1) + "+" + str(num2) + "=" + str(sum))

########################################################################
# Task 4:
# amount = int(input("How many apples are you buying?"))
# price = amount * 1.00
# print("the total cost is " + str(price))

########################################################################
# Task 5:
# age1 = int(input("Whats your age personA?"))
# age2 = int(input("Whats your age personB?"))
# if age1 < age2:
#     print("personA is younger than personB")
# elif age1 > age2:
#     print("personA is older than personB")
# else:
#     print("personA has the same age as personB")

########################################################################
# Task 6:
# password = "301014"
# guess = input("What is the password?")
# for count in range(3):
#     if guess == password:
#         print("Access Granted")
#     elif guess != password:
#         print("Access Denied, please try again later.")
#     else guess != pssword == 3:
#         print("system has been locked")

########################################################################
# Task 7:

# import random
# for count in range(10):

    
#     a=random.randint(1,100)
#     print(a)


########################################################################
# Task 8:

import random
for count in range(1):
    num1=random.randint(1,1000)
    num2=random.randint(1,1000)
    ans=(num1+num2)
    
    guess = int(input("What is " + str(num1) + "+" + str(num2)))
    if guess == ans:
        print("You are good at this")
    else:
        print("You are horrible at this")



########################################################################
# Additional exercises: