import tkinter as tk
import random

deck = []
player = []
dealer = []

def new_game():
    global deck, player, dealer
    deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    random.shuffle(deck)

    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    status.config(text="Your turn!")
    update()

def hit():
    player.append(deck.pop())

    if sum(player) > 21:
        status.config(text="Busted! You lose.")
    
    update()

def stand():
    while sum(dealer) < 17:
        dealer.append(deck.pop())

    if sum(dealer) > 21 or sum(player) > sum(dealer):
        status.config(text="You Win!")
    elif sum(player) < sum(dealer):
        status.config(text="Dealer Wins.")
    else:
        status.config(text="Push (Tie).")

    update()

def update():
    player_label.config(text=f"You: {player} ({sum(player)})")
    dealer_label.config(text=f"Dealer: {dealer} ({sum(dealer)})")

# para sa ui
root = tk.Tk()
root.title("Python Blackjack")
root.geometry("400x600")

status = tk.Label(root, text="Press 'New Game' to start.", font=("Arial", 12, "bold"))
status.pack(pady=10)

dealer_label = tk.Label(root, text="Dealer:", font=("Arial", 10))
dealer_label.pack()

player_label = tk.Label(root, text="You:", font=("Arial", 10))
player_label.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Hit", command=hit, width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Stand", command=stand, width=10).grid(row=0, column=1, padx=5)

tk.Button(root, text="New Game", command=new_game, width=20).pack(pady=10)

info_text = (
    "How it works:\n\n"
    "1. Goal: Get as close to 21 as possible without going over.\n"
    "2. Face cards (J, Q, K) are worth 10.\n"
    "3. Ace is worth 11 unless that total puts you\n"
    "   over 21, in which case it is worth 1.\n"
    "4. Dealer must hit until they have at least 17.\n"
    "5. Hit means you pull one more card.\n"
    "6. Stand means you stay on your current card (s)."
)

info_label = tk.Label(root, text=info_text, font=("Arial", 9),
                      justify="left", bg="#f0f0f0", padx=10, pady=10)
info_label.pack(fill="x", pady=20)

root.mainloop()