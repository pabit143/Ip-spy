#!/usr/bin/env python3

import requests
import argparse
from colorama import Fore, Style

def get_ip_info(ip=None):
    url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"
    try:
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'fail':
            print(f"{Fore.RED}[!] Error: {data['message']}{Style.RESET_ALL}")
            return

        print(f"{Fore.CYAN}[+] IP Info for: {data['query']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ZIP: {data['zip']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"ISP: {data['isp']}")
        print(f"Org: {data['org']}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[!] Failed to fetch IP info: {e}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="🔍 IP-Spy - IP Info Tracker by Pabit")
    parser.add_argument("-i", "--ip", help="IP address to track")
    args = parser.parse_args()

    get_ip_info(args.ip)

if __name__ == "__main__":
    main()
