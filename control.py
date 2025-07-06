import requests
from colorama import init, Fore, Style
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

def display():
    print(f"Eyes: arrows Misc: {Fore.YELLOW}T{Style.RESET_ALL}alk {Fore.RED}Q{Style.RESET_ALL}uit")
    print(f"Eyebrows: Norma{Fore.YELLOW}L{Style.RESET_ALL} Nast{Fore.YELLOW}Y{Style.RESET_ALL}")
    print(f"T-shirts: {Fore.YELLOW}B{Style.RESET_ALL}lackAlps "
          f"{Fore.YELLOW}G{Style.RESET_ALL}reHack "
          f"{Fore.YELLOW}I{Style.RESET_ALL}nsomnihack "
          f"{Fore.YELLOW}N{Style.RESET_ALL}orthSec "
          f"{Fore.YELLOW}P{Style.RESET_ALL}ass The Salt "
          f"{Fore.YELLOW}R{Style.RESET_ALL}adare2 "
          f"{Fore.YELLOW}V{Style.RESET_ALL}irus Bulletin ")

    
display()
while True:
    c = getch().lower()
    if c == '\x1b[A':
        print("up")
    elif c == '\x1b[B':
        print("down")
    elif c == '\x1b[C':
        print("right")
    elif c == '\x1b[D':
        print("left")
    elif c == "y": send("nasty")
    elif c == "l": send("normal")
    elif c == "b": send("blackalps")
    elif c == "g": send("grehack")
    elif c == "i": send("insomnihack")
    elif c == "n": send("nsec")
    elif c == "p": send("passthesalt")
    elif c == "r": send("radare")
    elif c == "v": send("vb")
    elif c == "t":
        print("\nEnter your message and press Enter:")
        # repasse en mode input normal
        message = input()
        say(message)
        print("Back to control mode. Press q to quit.")
    elif c == "q": break
