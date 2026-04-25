import requests
import time

def get_live_price(coin_id):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        data = requests.get(url).json()
        return data[coin_id]['usd']
    except:
        return "Price not found"

print("\n--- $RSW ENGINE INITIALIZING ---")
time.sleep(1)

# സൊലാനയുടെ ലൈവ് വില നോക്കുന്നു
sol_price = get_live_price('solana')
print(f"Current SOL Price: ${sol_price}")

if isinstance(sol_price, (int, float)) and sol_price > 145:
    print("Market Status: BULLISH 🚀")
    print("Welcome to the $RSW Project, Alpha.")
else:
    print("Market Status: ACCUMULATING 💎")

print("--------------------------------\n")


