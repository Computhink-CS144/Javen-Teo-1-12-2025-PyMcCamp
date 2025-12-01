# Write all your codes for Day 1 here.
# COMMENT out the previous task before going on to the next task
#print("hello from day1")

########################################################################
# Task 1:
# print("Hello o Mighty One")


########################################################################
# Task 2:
print("My name is Javen")
print("I am 11 years old")
print("I attend Ai Tong School")
print("If I had 2000 dollars as a reward, I would buy a phone for my Father")
########################################################################
# Task 3:
animal1="Tiger"
animal2="Lion"
animal3="T-Rex"
print(animal1)
print(animal2)
print(animal3)
########################################################################
# Task 4:
num1=8
num2=4
print(num1+num2)
print(num1*num2)
print(num1/num2)
print(num1-num2)

########################################################################
# Task 5:
name="Dog"
food="bones"
print("My name is " + name + " and I like to eat " + food)

########################################################################
# Task 6:
def info():
    print("My name is Javen")
    print("I am 11 years old")
    print("I attend Ai Tong School")
    print("If I had 2000 dollars as a reward, I would buy a phone for my Father")
info()
########################################################################
# Task 7:
def addition(num1, num2):
    print(num1 + num2)

addition(1, 999999999999999999999999999999999999999999999999999999999999999999)



########################################################################
# Additional exercises:
def teleport():
    agent.teleport_to_player()
def forward(steps):
    agent.move(FORWARD, steps)
def back(steps):
    agent.move(BACK, steps)
def up(height):
    agent.move(UP, height)
def down(height):
    agent.move(DOWN, height)
def tr():
    agent.turn(RIGHT)
def tl():
    agent.turn(LEFT)

def obby1():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)

player.on_chat("come", teleport)
player.on_chat("fw", forward)
player.on_chat("bk", back)
player.on_chat("up", up)
player.on_chat("down", down)
player.on_chat("tr", tr)
player.on_chat("tl", tl)
player.on_chat("obby1",obby1)