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

RSW_BALANCE = 1542.0  # നിന്റെ ഇപ്പോഴത്തെ ബാലൻസ്
WALET_ID = "RSW_vX98_OGP_ADEP"

while True:
    os.system('clear')
    
    # RANK SYSTEM LOGIC
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
    print(f">> Network: {GREEN}RSW TESTNET-ALPHA ✅{END}")
    print(f">> Mode: {RED}BOOSTER ACTIVE ⚡⚡{END}")
    print(f">> Your Rank: {RANK}")
    
    print(f"\n{BOLD}[YOUR ASSETS]{END}")
    print(f">> RSW Balance: {GREEN}{BOLD}{round(RSW_BALANCE, 2)} RSW{END}")
    
    # MINING LOGIC
    mining_speed = random.uniform(5.0, 25.0)
    
    if random.random() < 0.2:
        bonus = random.randint(50, 200)
        RSW_BALANCE += bonus
        print(f"\n{RED}{BOLD}[!!! MEGA JACKPOT !!!]{END}")
        print(f"{RED}>> Bonus Received: +{bonus} RSW 🚀🔥{END}")
    
    RSW_BALANCE += mining_speed
    
    print(f"\n{BOLD}[MINING LIVE]{END}")
    print(f">> Speed: {BLUE}{round(mining_speed, 2)} RSW/sec{END}")
    print(f">> Status: {GREEN}High Speed Mining...{END}")
    
    print(f"\n{BLUE}-------------------------------------{END}")
    print(f"Updating in 1 second... {YELLOW}(CTRL+C to Stop){END}")
    
    time.sleep(1)

