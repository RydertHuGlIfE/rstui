import ui
import connector
import scp_handler
from colorama import Fore, Style


def main():
    ui.print_ban()
    user, host, password = connector.getconn()

    if connector.test_ssh(user, host, password):
        print(Fore.GREEN + "Connected!" + Style.RESET_ALL)
        scp_handler.smenu(user, host, password)
    else:
        print(Fore.RED + "Connection Failed." + Style.RESET_ALL)

if __name__ == '__main__':
    main()