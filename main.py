import ui
import connector
import scp_handler
from colorama import Fore, Style
import threading
import time,sys


spinchar = ['|', '/', '-', '\\']

def main():
    ui.print_ban()
    user, host, password = connector.getconn()

    result = []
    def ssh_wrapper():
        result.append(connector.test_ssh(user, host, password))

    t1 = threading.Thread(target=ssh_wrapper)
    t1.start()

    i = 0
    while t1.is_alive():
        sys.stdout.write("\r" + "Connecting.... " + spinchar[i % 4])
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1

    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

    t1.join()

    if result[0]:
        print(Fore.GREEN + "Connected!" + Style.RESET_ALL)
        scp_handler.smenu(user, host, password)
    else:
        print(Fore.RED + "Connection Failed." + Style.RESET_ALL)

if __name__ == '__main__':
    main()