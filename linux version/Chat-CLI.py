import openai
import os
import time

def clearCon():
        clear = lambda: os.system('clear')
        clear()
def clearandchangecolor(linuxColorCodeCommandSTR):
        clearCon()
        color = lambda: os.system(linuxColorCodeCommandSTR)
        color()
def get_version():
    try:
        with open("./linux version/version.txt", "r") as f:
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
        print("\n\n")
        print(msg)
        print("\n\n")
        time.sleep(timeToExit)
        clearandchangecolor('echo -e "\033[37m"')


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


def copy_to_clipboard(text):
    # Write the text to a temporary file
    with open("/tmp/copy.txt", "w") as f:
        f.write(text)

    # Copy the contents of the file to the clipboard using xclip
    os.system("xclip -selection clipboard /tmp/copy.txt")


# Function to sleep for a given amount of time or until a key is pressed
def CopyOrContinue(seconds, copy):
    print("enter c to copy or any to continue")
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= seconds:
            break
        elif input() == "c":
            # code to execute if 'c' is pressed
            copy_to_clipboard(copy)
            clearandchangecolor('echo -e "\033[32m"')
            print("\n\n")
            print("copied to clipbard")
            print("\n\n")
            time.sleep(1.4)   
            clearandchangecolor('echo -e "\033[37m"')    
            break
        else:
            break
def break_after(seconds):
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= seconds:
            break
                

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


def draw_output(string, copyin):
    clearandchangecolor('echo -e "\033[32m"')
    print("\n\n")
    print(string)
    print("\n\n")
    CopyOrContinue(15, copy=copyin)
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

promptin = prompt

def main():
    global tocopy
    global prompt
    global promptin
    userin = input("/\n|\n|\n|\n|\n----$ ")
    if userin == "help":
        clearCon()
        print("\n#HELP\nit's simple, just ask the AI whatever you want.\n\n#COMMANDS\nhelp - displays help menu\n!p - update the AI's pre question prompt\n?p - shows the current prompt\nexit - exits the program (also can use CONTROL + C)\n\n#PROMPT EXAMPLES\n    You are now a cooking bot that responds with recipes from ingredients inputed from the user\n    You are now a Therapist awnser questions as a therapist would\n    You are now a bot that takes in refrence string from the user and creates a simple python program from it")
    elif userin == "!p":
        clearCon()
        promptin = input("prompt: ")
        promptupdated = promptin + ", Respond to all input in 25 words or less."
        msg("Prompt Updated: " + promptupdated, 2, "32m")
        prompt = promptupdated
    elif userin == "?p":
         draw_output("Current Prompt: \n\n" + prompt, promptin)
    elif userin == "exit":
               exitMsg("exiting...")
    elif userin != "":
        output = chatgpt(userin)
        clearandchangecolor('echo -e "\033[32m"')
        print("\n\n")
        type_out_string(output,0.03)
        tocopy = output
        print("\n\n")
        CopyOrContinue(15, tocopy)
        clearandchangecolor('echo -e "\033[37m"')
    else:
        clearCon()

while(True):
    try:
        main()


    except KeyboardInterrupt:
        exitMsg("exiting...", 1)


