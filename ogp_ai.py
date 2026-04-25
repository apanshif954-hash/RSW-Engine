import time
import os
import random

# --- COLORS ---
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

BAL_FILE = "balance.txt"

# ബാലൻസ് ഫയലിൽ നിന്ന് വായിക്കാനുള്ള ഫങ്ക്ഷൻ
def load_balance():
    if os.path.exists(BAL_FILE):
        with open(BAL_FILE, "r") as f:
            return float(f.read())
    return 7182.0  # ഫയൽ ഇല്ലെങ്കിൽ നിന്റെ ഇപ്പോഴത്തെ ബാലൻസിൽ നിന്ന് തുടങ്ങും

# ബാലൻസ് ഫയലിലേക്ക് സേവ് ചെയ്യാനുള്ള ഫങ്ക്ഷൻ
def save_balance(bal):
    with open(BAL_FILE, "w") as f:
        f.write(str(bal))

RSW_BALANCE = load_balance()
WALET_ID = "RSW_vX98_OGP_ADEP"

try:
    while True:
        os.system('clear')
        
        # RANK SYSTEM
        if RSW_BALANCE < 2000:
            RANK = f"{RED}BRONZE MINER{END}"
        elif RSW_BALANCE < 5000:
            RANK = f"{YELLOW}SILVER MINER{END}"
        elif RSW_BALANCE < 10000:
            RANK = f"{BLUE}GOLD MINER{END}"
        else:
            RANK = f"{GREEN}{BOLD}SIGMA DEVELOPER 🗿{END}"

        print(f"{BLUE}====================================={END}")
        print(f"{BLUE}{BOLD}      OGP AI (ADEP) - RSW ENGINE     {END}")
        print(f"{BLUE}====================================={END}")
        
        print(f"\n{BOLD}[SYSTEM STATUS]{END}")
        print(f">> Wallet ID: {YELLOW}{WALET_ID}{END}")
        print(f">> Rank: {RANK}")
        print(f">> Data Saving: {GREEN}ENABLED ✅{END}")
        
        print(f"\n{BOLD}[YOUR ASSETS]{END}")
        print(f">> RSW Balance: {GREEN}{BOLD}{round(RSW_BALANCE, 2)} RSW{END}")
        
        # MINING
        mining_speed = random.uniform(5.0, 25.0)
        RSW_BALANCE += mining_speed
        
        # ഓരോ തവണയും ഫയലിലേക്ക് സേവ് ചെയ്യുന്നു
        save_balance(RSW_BALANCE)
        
        print(f"\n{BOLD}[MINING LIVE]{END}")
        print(f">> Speed: {BLUE}{round(mining_speed, 2)} RSW/sec{END}")
        
        print(f"\n{BLUE}-------------------------------------{END}")
        print(f"Updating... {YELLOW}(CTRL+C to Stop & Save){END}")
        
        time.sleep(1)

except KeyboardInterrupt:
    print(f"\n{YELLOW}Stopping... Progress Saved Successfully!{END}")

