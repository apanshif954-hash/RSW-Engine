import time
import os
import random

# --- COLORS ---
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
BOLD = '\033[1m'
END = '\033[0m'

BAL_FILE = "balance.txt"
RSW_PRICE = 4.25  
SOL_PRICE = 12000.0 # ഒരു സോളാനയുടെ വില ഏകദേശം ₹12,000

def load_balance():
    if os.path.exists(BAL_FILE):
        try:
            with open(BAL_FILE, "r") as f:
                return float(f.read())
        except: return 10885.0
    return 10885.0

def save_balance(bal):
    with open(BAL_FILE, "w") as f:
        f.write(str(bal))

RSW_BALANCE = load_balance()
SOL_BALANCE = 0.0 # പുതിയ കോയിൻ
WALET_ID = "RSW_vX98_OGP_ADEP"

try:
    while True:
        os.system('clear')
        
        # RANK SYSTEM
        if RSW_BALANCE < 10000:
            RANK = f"{YELLOW}GOLD MINER{END}"
        elif RSW_BALANCE < 50000:
            RANK = f"{CYAN}PLATINUM EXTRACTOR{END}"
        else:
            RANK = f"{GREEN}{BOLD}SIGMA DEVELOPER 🗿{END}"

        inr_value = (RSW_BALANCE * RSW_PRICE) + (SOL_BALANCE * SOL_PRICE)

        print(f"{BLUE}====================================={END}")
        print(f"{BLUE}{BOLD}     RSW & SOL MULTI-ENGINE v3.0     {END}")
        print(f"{BLUE}====================================={END}")
        
        print(f"\n{BOLD}[PROFILE]{END} >> {RANK}")
        print(f">> Wallet: {YELLOW}{WALET_ID}{END}")
        
        print(f"\n{BOLD}[CRYPTO ASSETS]{END}")
        print(f">> {GREEN}RSW Balance:{END} {BOLD}{round(RSW_BALANCE, 2)} RSW{END}")
        print(f">> {CYAN}SOL Balance:{END} {BOLD}{round(SOL_BALANCE, 4)} SOL{END}")
        print(f">> Total Value: {YELLOW}{BOLD}₹{round(inr_value, 2)}{END}")
        
        # MINING LOGIC
        rsw_speed = random.uniform(10.0, 35.0)
        sol_speed = random.uniform(0.0001, 0.0005) # സോളാന പതുക്കെ മൈൻ ചെയ്യും (വില കൂടുതലായതുകൊണ്ട്)
        
        RSW_BALANCE += rsw_speed
        SOL_BALANCE += sol_speed
        save_balance(RSW_BALANCE)
        
        print(f"\n{BOLD}[LIVE MINING]{END}")
        print(f">> RSW Speed: {BLUE}{round(rsw_speed, 2)} RSW/sec{END}")
        print(f">> SOL Speed: {CYAN}{round(sol_speed, 6)} SOL/sec{END}")
        
        print(f"\n{BLUE}-------------------------------------{END}")
        print(f"Updating... {YELLOW}(CTRL+C to Save & Exit){END}")
        
        time.sleep(1)

except KeyboardInterrupt:
    save_balance(RSW_BALANCE)
    print(f"\n{YELLOW}Data Saved! See you, SIGMA!{END}")

