import random

def start_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    
    print("--- NUMBER GUESSING GAME ---")
    print("ഞാൻ 1 മുതൽ 20 വരെ ഉള്ള ഒരു നമ്പർ വിചാരിച്ചിട്ടുണ്ട്. അത് ഏതാണെന്ന് പറയാമോ?")

    while True:
        guess = int(input("നിങ്ങളുടെ ഊഹം ടൈപ്പ് ചെയ്യൂ: "))
        attempts += 1

        if guess < secret_number:
            print("അല്പം കൂടി വലിയ നമ്പർ നോക്കൂ..")
        elif guess > secret_number:
            print("അല്പം കൂടി ചെറിയ നമ്പർ നോക്കൂ..")
        else:
            print(f"അടിപൊളി! {attempts} വട്ടം ശ്രമിച്ചപ്പോൾ നിങ്ങൾ ശരിയായ നമ്പർ കണ്ടെത്തി!")
            break

start_game()
thon game.py

