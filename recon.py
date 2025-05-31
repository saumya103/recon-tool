import socket
import requests
import whois

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Address: {ip}")
    except:
        print("[-] Could not resolve domain.")

def get_headers(domain):
    try:
        response = requests.get("http://" + domain)
        print("\n[+] HTTP Headers:")
        for key, value in response.headers.items():
            print(f"   {key}: {value}")
    except:
        print("[-] Could not fetch headers.")

def get_whois(domain):
    try:
        info = whois.whois(domain)
        print("\n[+] WHOIS Info:")
        print(f"   Domain Name: {info.domain_name}")
        print(f"   Registrar: {info.registrar}")
        print(f"   Creation Date: {info.creation_date}")
    except:
        print("[-] WHOIS lookup failed.")

if __name__ == "__main__":
    domain = input("Enter domain (e.g. example.com): ")
    get_ip(domain)
    get_headers(domain)
    get_whois(domain)
