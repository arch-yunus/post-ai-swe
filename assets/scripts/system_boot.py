"""
KTU SOFTWARE ENGINEERING - STRATEGIC COMMAND CENTER
SYSTEM BOOT SEQUENCE (SIMULATION)

Author: @bahattinyunus (Strategic Architect)
Protocol: God Tier
"""

import time
import sys
import random

def type_effect(text, delay=0.03):
    """Simulates typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_logo():
    logo = """
    ██   ██ ████████ ██    ██      ███████ ███████ 
    ██  ██     ██    ██    ██      ██      ██      
    █████      ██    ██    ██      ███████ █████   
    ██  ██     ██    ██    ██           ██ ██      
    ██   ██    ██     ██████       ███████ ███████ 
    
    [STRATEGIC COMMAND CENTER - ONLINE]
    """
    print("\033[96m" + logo + "\033[0m") 

def system_check():
    checks = [
        "[KERNEL] Loading Core Modules...",
        "[NETWORK] Connecting to Trabzon/Of Mainframe...",
        "[AUTH] Verifying Identity: @bahattinyunus...",
        "[CRYPTO] Decrypting 'MUREDDAAT' Layer...",
        "[AI] Synchronizing Neural Interfaces...",
        "[STATUS] SYSTEM OPTIMAL."
    ]
    
    for check in checks:
        time.sleep(random.uniform(0.2, 0.8))
        if "[STATUS]" in check:
            print(f"\033[92m{check}\033[0m")
        else:
            print(check)

def main():
    print_logo()
    time.sleep(1)
    print("-" * 50)
    system_check()
    print("-" * 50)
    time.sleep(0.5)
    type_effect("\n>>> WELCOME, ARCHITECT.", 0.1)
    type_effect(">>> Awaiting operational commands...", 0.05)

if __name__ == "__main__":
    main()
