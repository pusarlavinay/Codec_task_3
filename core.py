import os
import sys
import subprocess

def main():
    while True:
        print("\n=== Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. HTTP Info")
        print("3. Password Audit")
        print("4. Exit")
        
        choice = input("\nSelect an option: ")

        if choice == "1":
            target = input("Enter target IP/hostname: ")
            os.system(f"python3 modules/port_scanner.py {target}")
        
        elif choice == "2":
            url = input("Enter URL: ")
            os.system(f"python3 http_info.py {url}")
        
        elif choice == "3":
            wordlist = input("Enter path to password wordlist: ")
            os.system(f"python3 passwd.audit.py {wordlist}")
        
        elif choice == "4":
            print("Exiting toolkit...")
            sys.exit()
        
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
