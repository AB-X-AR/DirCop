print("""########     ####    ########      ######      #######     ########  
##     ##     ##     ##     ##    ##    ##    ##     ##    ##     ## 
##     ##     ##     ##     ##    ##          ##     ##    ##     ## 
##     ##     ##     ########     ##          ##     ##    ########  
##     ##     ##     ##   ##      ##          ##     ##    ##        
##     ##     ##     ##    ##     ##    ##    ##     ##    ##        
########     ####    ##     ##     ######      #######     ##       
                     DIRCOP - Directory Finder Tool
                     Author: ABXAR | License: MIT
                          === FOLLOW ME ON ===
                     X : https://x.com/ABXAR_7x30

""")



# DirCop made by AB-X-AR
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor


def load_payloads(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        exit(1)


def check_path(url, payload):
    target_url = f"{url.rstrip('/')}/{payload.lstrip('/')}"
    try:
        response = requests.get(target_url, timeout=5)
        if response.status_code == 200:
            print(f"[FOUND] {target_url} [200 OK]")
            return target_url
        elif response.status_code in [401, 403]:
            print(f"[RESTRICTED] {target_url} [{response.status_code}]")
        elif response.status_code == 302:
            print(f"[REDIRECT] {target_url} [302 Found]")
    except requests.RequestException as e:
        print(f"[ERROR] Could not connect to {target_url} ({e})")
    return None


def scan_directory(url, payloads, threads=10):
    found_paths = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda payload: check_path(url, payload), payloads)
        for result in results:
            if result:
                found_paths.append(result)
    return found_paths


def main():
    parser = argparse.ArgumentParser(description="DirCop - Simple Directory Scanner")
    parser.add_argument("-u", "--url", required=False, help="Target URL (e.g., http://example.com)")
    parser.add_argument("-w", "--wordlist", required=False, help="Path to wordlist file")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default: 10)")
    args = parser.parse_args()

    if not args.url:
        args.url = input("Enter the target URL (e.g., http://example.com): ").strip()
    if not args.wordlist:
        args.wordlist = input("Enter the path to the payload file: ").strip()

    payloads = load_payloads(args.wordlist)
    found_paths = scan_directory(args.url, payloads, threads=args.threads)

    if found_paths:
        print("\n[+] Summary of Found Paths:")
        for path in found_paths:
            print(path)
    else:
        print("\n[-] No accessible paths found.")


if __name__ == "__main__":
    main()
