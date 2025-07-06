import requests
from colorama import init, Fore, Style
import sys, termios, tty, requests
import time

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

def display():
    print(f"Eyes: Arrows Misc: {Fore.YELLOW}T{Style.RESET_ALL}alk {Fore.RED}Q{Style.RESET_ALL}uit")
    print(f"Eyebrows: Norma{Fore.YELLOW}L{Style.RESET_ALL} Nast{Fore.YELLOW}Y{Style.RESET_ALL} "
          f"Trousers: Bl{Fore.BLUE}U{Style.RESET_ALL}e Bro{Fore.YELLOW}W{Style.RESET_ALL}n" )
    print(f"T-shirts: {Fore.YELLOW}B{Style.RESET_ALL}lackAlps "
          f"{Fore.YELLOW}G{Style.RESET_ALL}reHack "
          f"{Fore.RED}I{Style.RESET_ALL}nsomnihack "
          f"{Fore.BLUE}N{Style.RESET_ALL}orthSec "
          f"{Fore.RED}P{Style.RESET_ALL}assTheSalt "
          f"{Fore.YELLOW}R{Style.RESET_ALL}adare2 "
          f"{Fore.GREEN}V{Style.RESET_ALL}irusBulletin ")
    print(f"Sequence: {Fore.ORANGE}1{Style.RESET_ALL}1")          

def sequence1():
    send("nasty")
    send("left")
    time.sleep(1)
    send("normal")         
    send("up")
    time.sleep(1)
    send("nasty")
    send("right")
    time.sleep(1)
    send("normal")
    send("down")
    time.sleep(1)
    send("right")

    
display()
while True:
    c = getch().lower()
    if c == '\x1b':
        # beginning of an arrow
        c += getch()
        c += getch()
        if c == '\x1b[A':
            send("up")
        elif c == '\x1b[B':
            send("down")
        elif c == '\x1b[C':
            send("right")
        elif c == '\x1b[D':
            send("left")
    elif c == "y": send("nasty")
    elif c == "l": send("normal")
    elif c == "b": send("blackalps")
    elif c == "g": send("grehack")
    elif c == "i": send("insomnihack")
    elif c == "n": send("nsec")
    elif c == "p": send("pst")
    elif c == "r": send("radare")
    elif c == "v": send("vb")
    elif c == "u": send("blue")
    elif c == "w": send("brown")
    elif c == '1': sequence1()
    elif c == "t":
        print("\nEnter your message and press Enter:")
        # repasse en mode input normal
        message = input()
        say(message)
        print("Back to control mode. Press q to quit.")
    elif c == "q": break
