# toolkit.py
import os

# Function to display menu options
def show_menu():
    print("Termux Ethical Hacking Toolkit")
    print("1. Information Gathering")
    print("2. Brute Force Attacks")
    print("3. Wi-Fi Pentesting")
    print("4. Phishing")
    print("5. Anonymity Tools")
    print("6. Exit")

# Function for Information Gathering
def info_gathering():
    os.system("echo 'Running information gathering...'")

# Function for Brute Force Attacks
def brute_force():
    os.system("echo 'Running brute-force attacks...'")

# Function for Wi-Fi Pentesting
def wifi_pentesting():
    os.system("echo 'Running Wi-Fi pentesting...'")

# Function for Phishing
def phishing():
    os.system("echo 'Running phishing attack...'")

# Function for Anonymity Tools (VPN, Tor, etc.)
def anonymity_tools():
    os.system("echo 'Setting up anonymity tools...'")

# Main function to run the menu and get user input
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            info_gathering()
        elif choice == '2':
            brute_force()
        elif choice == '3':
            wifi_pentesting()
        elif choice == '4':
            phishing()
        elif choice == '5':
            anonymity_tools()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# Import the module at the top of the file
from modules.recon import gather_info

def info_gathering():
    gather_info()
