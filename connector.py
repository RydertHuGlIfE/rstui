import subprocess
import getpass
from colorama import Fore, Style
import colorama
colorama.init(autoreset=True)

def getconn():
    user     = input(Fore.CYAN + "Username: " + Style.RESET_ALL).strip()
    host     = input(Fore.CYAN + "Host/IP:  " + Style.RESET_ALL).strip()
    password = getpass.getpass(Fore.CYAN + "Password: " + Style.RESET_ALL)
    return user, host, password

def test_ssh(user, host, password):
    result = subprocess.run(
        ["sshpass", "-p", password, "ssh", f"{user}@{host}", "exit"]
    )
    return result.returncode == 0
