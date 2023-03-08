import getch
import openai
import os
import time
import pyperclip
def clearCon():
        clear = lambda: os.system('clear')
        clear()
def clearandchangecolor(linuxColorCodeCommandSTR):
        clearCon()
        color = lambda: os.system(linuxColorCodeCommandSTR)
        color()
def get_version():
    try:
        with open("./version.txt", "r") as f:
            version = f.read().strip()
        return version
    except:
         return "version.txt missing"
def bootmenu():
    print("   _     _     _     _     _     _     _     _  ")
    print("  / \   / \   / \   / \   / \   / \   / \   / \ ")
    print(" ( C ) ( h ) ( a ) ( t ) ( - ) ( c ) ( l ) ( i )")
    print("  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ ")
    type_out_string("---------------",0.1)
    print ("version: " + str(get_version())) 
    time.sleep(2)
def msg(msg, timeToExit, linuxcolorString):
        clearandchangecolor('echo -e "\033[' + linuxcolorString + '"')
        print(msg)
        time.sleep(timeToExit)
        clearandchangecolor('echo -e "\033[37m"')
        exit(0)


def get_api_key():
    with open("./ai.txt", "r") as f:
        api_key = f.read().strip()
    return api_key

    
def exitMsg(msg, timeToExit):
        clearandchangecolor('echo -e "\033[32m"')
        print(msg)
        time.sleep(timeToExit)
        clearandchangecolor('echo -e "\033[37m"')
        exit(0)

def sleep_interruptable(tim, copyAble):
    global tocopy
    start_time = time.monotonic()
    if copyAble == True:
        print("Press Enter or c to set clipboard")
    else:
        print("Press Enter")
    while time.monotonic() - start_time < tim:
        if getch.kbhit():
            key = getch.getch()
            if key == b'\r':  # Enter key
                return
            elif key == b'c' and copyAble == True:  # c key
                pyperclip.copy(tocopy)
                draw_output_ni("Copied to clipboard",1)
                time.sleep(1)
                return
                

def chatgpt(chat):
    global messages
    global prompt

    messages.append({"role": "user", "content": prompt + chat})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    chat_transcript = system_message['content']


    return chat_transcript

def init():
    clearCon()
    if get_api_key() == "REPLACE WITH YOUR OPENAI API KEY":
        msg("_ERROR_\nAPI KEY NOT SET\n    Please open ai.txt and paste your openai api key in there\n    If you do not have ai.txt simply create the text document and paste in your api key",8,"31m")
    else:
        bootmenu()
         
def set_clipboard(text):
    pyperclip.copy(text)

def draw_output(string):
    clearandchangecolor('echo -e "\033[32m"')
    print("\n\n")
    print(string)
    print("\n\n")
    sleep_interruptable(15, copyAble=False)
    clearandchangecolor('echo -e "\033[37m"')

def draw_output_ni(string, timeToSleep):
    clearandchangecolor('echo -e "\033[32m"')
    print("\n\n")
    print(string)
    print("\n\n")
    time.sleep(timeToSleep)
    clearandchangecolor('echo -e "\033[37m"')

def type_out_string(text, typing_speed):

    for character in text:
        print(character, end='', flush=True)
        time.sleep(typing_speed)
    print()

init()

openai.api_key = get_api_key()

prompt = "You are chatGPT AI. Respond to all input in 25 words or less." 

messages = [{"role": "system", "content": prompt}]

tocopy = ""

def main():
    global tocopy
    global prompt
    userin = input("/\n|\n|\n|\n|\n----$ ")
    if userin == "help":
        clearCon()
        print("\n#HELP\nit's simple, just ask the AI whatever you want.\n\n#COMMANDS\nhelp - displays help menu\n!p - update the AI's pre question prompt\n?p - shows the current prompt\nexit - exits the program (also can use CONTROL + C)\n\n#PROMPT EXAMPLES\n    You are now a cooking bot that responds with recipes from ingredients inputed from the user\n    You are now a Therapist awnser questions as a therapist would\n    You are now a bot that takes in refrence string from the user and creates a simple python program from it")
    elif userin == "!p":
        clearCon()
        promptin = input("prompt: ")
        promptin = promptin + ", Respond to all input in 25 words or less."
        draw_output("Prompt Updated: " + promptin)
        prompt = promptin
    elif userin == "?p":
         draw_output("Current Prompt: \n\n" + prompt)
    elif userin == "exit":
               exitMsg("exiting...")
    elif userin != "":
        output = chatgpt(userin)
        clearandchangecolor('echo -e "\033[32m"')
        print("\n\n")
        type_out_string(output,0.03)
        tocopy = output
        print("\n\n")
        sleep_interruptable(15, copyAble=True)
        clearandchangecolor('echo -e "\033[37m"')
    else:
        clearCon()

while(True):
    try:
        main()


    except KeyboardInterrupt:
        exitMsg("exiting...")


