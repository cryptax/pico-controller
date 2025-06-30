import requests
import sys, termios, tty, requests

def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch

def send(action):
    print(f'Sending {action}')
    requests.post("http://localhost:5000/action", data={"action": action})

def say(message):
    print(f'Sending message: {message}')
    requests.post("http://localhost:5000/say", data={"message": message})
    
print("Press w=up a=left d=right g=nasty n=normal t=say q=quit")
while True:
    c = getch()
    if c == "w": send("up")
    elif c == "a": send("left")
    elif c == "d": send("right")
    elif c == "g": send("nasty")
    elif c == "n": send("normal")
    elif c == "t":
        print("\nEnter your message and press Enter:")
        # repasse en mode input normal
        message = input()
        say(message)
        print("Back to control mode. Press q to quit.")
    elif c == "q": break
