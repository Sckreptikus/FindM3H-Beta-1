#!/usr/bin/env python3


try:
    from colorama import init, Fore, Style

except ModuleNotFoundError as e:
    print(f"[-] error: {e}")
    print(
        "[!] please install the requirements: $ sudo -H pip3 install -r requirements.txt"
    )
    sys.exit(1)


def print_banner(version):

    print(
        f"""
  ___   _   _ __    ____    _ ___  ___ _     _     _   _    
 |  _| | | | '_  \ |  _ \  | '_  \/  _' |  _| |   | |_| |  
 | |_  | | | | | | | | | | | | |____| | | |__ |   |     |   
 | __| | | | | | | | |_| | | |        | |  _| |   |  _  |    
 |_|   |_| |_| |_| |____/  |_|        |_| |___|   |_| |_|    
       {Fore.GREEN}Version: {version} | Author: Anonhack990, Inspired By: decoxviii{Fore.RESET}           /_/    /____/\n\n"""
    )
