import time
import os
import random

# --- OGP AI (ADEP) - RSW ENGINE ---
RSW_BALANCE = 1011.0  # നിന്റെ ഇപ്പോഴത്തെ ബാലൻസ്
WALET_ID = "RSW_vX98_OGP_ADEP"

while True:
    os.system('clear')
    print("=====================================")
    print("      OGP AI (ADEP) - RSW ENGINE     ")
    print("=====================================")
    print(f"\n[SYSTEM STATUS]")
    print(f">> Wallet ID: {WALET_ID}")
    print(f">> Network: RSW TESTNET-ALPHA ✅")
    
    print(f"\n[YOUR ASSETS]")
    print(f">> RSW Balance: {round(RSW_BALANCE, 2)} RSW")
    
    # --- TURBO MINING LOGIC ---
    mining_speed = random.uniform(0.5, 5.0)
    
    # 10% ചാൻസിൽ ജാക്ക്പോട്ട് ബോണസ്
    if random.random() < 0.1:
        bonus = random.randint(10, 50)
        RSW_BALANCE += bonus
        print(f"\n[!!! JACKPOT !!!]")
        print(f">> Bonus Received: +{bonus} RSW 🚀")
    
    RSW_BALANCE += mining_speed
    
    print(f"\n[MINING LIVE]")
    print(f">> Speed: {round(mining_speed, 2)} RSW/sec")
    print(f">> Status: Mining RSW Coins...")
    
    print("\n-------------------------------------")
    print("Updating in 5 seconds... (CTRL+C to Stop)")
    time.sleep(5)

