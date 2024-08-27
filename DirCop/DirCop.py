#DirCop made by AB-X-AR
import requests
def load_payloads(file_path):
    with open(file_path, 'r') as file:
        payloads = file.read().splitlines()
    return payloads

def scan_directory(url, payloads):
    found_paths = []
    for payload in payloads:
        target_url = f"{url}/{payload}"
        response = requests.get(target_url)
        if response.status_code == 200:
            print(f"[FOUND] {target_url}")
            found_paths.append(target_url)
        
    return found_paths

def main():
    #Set Target Here
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
    
    #Select Payload file
    payload_file = input("Enter the path to the payload file: ").strip()
    payloads = load_payloads(payload_file) 
    found_paths = scan_directory(target_url, payloads)
    
    
    if found_paths:
        print("\nSummary of found paths:") #Printing Founded Paths
        for path in found_paths:
            print(path)
    else:
        print("\nNo paths found.")

if __name__ == "__main__":
    main()
