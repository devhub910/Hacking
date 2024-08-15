import os
import time
import colorama
from colorama import Fore, Style
import re

# Initialize colorama
colorama.init()

def ping_site(site):
    try:
        # Ping command
        while True:
            response = os.popen(f"ping -n 1 {site}").read()
            if "TTL=" in response:
                # Extract IP and time
                ip_match = re.search(r"\[(.*?)\]", response)
                time_match = re.search(r"time=(.*?)ms", response)
                
                ip = ip_match.group(1) if ip_match else "unknown"
                time_ping = time_match.group(1) if time_match else "<1"
                
                print(f"{Fore.GREEN}Connected to {ip} : time={time_ping}ms  protocol=TCP  port=80{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Connection timed out{Style.RESET_ALL}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Ping stopped by user.")

if __name__ == "__main__":
    site = input("URL PING > ")
    ping_site(site)