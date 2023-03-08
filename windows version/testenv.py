import platform
def check_system():
    system = platform.system()
    if system == "Windows":
        print("The current system is running on Windows")
    elif system == "Linux":
        print("The current system is running on Linux")
    else:
        print("Unknown system")
check_system()