# modules/recon.py
import os

def gather_info():
    domain = input("Enter domain for WHOIS lookup: ")
    os.system(f"whois {domain}")
