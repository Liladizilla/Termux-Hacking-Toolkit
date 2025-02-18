#!/bin/bash
# Install required packages for Termux Ethical Hacking Toolkit

echo "Installing required packages..."

# Update and upgrade Termux packages
pkg update -y
pkg upgrade -y

# Install essential tools
pkg install python -y      # Python for scripting
pkg install git -y         # Git for version control
pkg install nmap -y        # Nmap for network scanning
pkg install tor -y         # Tor for anonymity
pkg install proxychains -y # Proxychains for routing through proxies
pkg install metasploit -y  # Metasploit for penetration testing

echo "All required packages installed!"
