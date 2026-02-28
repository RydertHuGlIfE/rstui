import ui
import connector
import scp_handler
from colorama import Fore, Style
import threading 


def main():
    ui.print_ban()
    user, host, password = connector.getconn()
    t1 = threading.Thread(target=connector.test_ssh, args=(user, host, password))
    t1.start()

    if t1.is_alive():
        t1.join()
        print(Fore.GREEN + "Connected!" + Style.RESET_ALL)
        scp_handler.smenu(user, host, password)
    else:
        print(Fore.RED + "Connection Failed." + Style.RESET_ALL)

if __name__ == '__main__':
    main()