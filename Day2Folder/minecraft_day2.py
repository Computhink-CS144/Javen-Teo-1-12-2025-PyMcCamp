# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
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

def chop(height):
    for count in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()
    agent.move(RIGHT, 1)

def mine(height):
    for count in range(height):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        agent.destroy(FORWARD)
        agent.destroy(BACK)
        agent.destroy(RIGHT)
        agent.destroy(LEFT)
        agent.collect_all()
    agent.move(UP, height)

def bulldoze(height):
    for count in range(height):
        agent.destroy(FORWARD)
        agent.destroy(RIGHT)
        agent.destroy(LEFT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
    agent.move(BACK, height)
    agent.move(DOWN, 1)

player.on_chat("come", teleport)
player.on_chat("fw", forward)
player.on_chat("bk", back)
player.on_chat("up", up)
player.on_chat("down", down)
player.on_chat("tr", tr)
player.on_chat("tl", tl)
player.on_chat("obby1",obby1)
player.on_chat("chop",chop)
player.on_chat("mine", mine)
player.on_chat("bulldoze", bulldoze)