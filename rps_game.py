import random

print("✊ ROCK PAPER SCISSORS ✌️")
print("Computer ke khilaaf khel bhai\n")

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    print(f"Score: Tu {user_score} - {computer_score} Computer")
    user_choice = input("Chun le: rock/paper/scissors (q = quit): ").lower()
    
    if user_choice == 'q':
        print(f"\nFinal Score: Tu {user_score} - {computer_score} Computer")
        if user_score > computer_score:
            print("🏆 JEET GAYA BHAI! LEGEND")
        elif user_score < computer_score:
            print("Computer jeet gaya 😅 Phir try kar")
        else:
            print("DRAW! Barabri ka muqabla 🤝")
        break
        
    if user_choice not in options:
        print("Galat input bhai! rock, paper ya scissors likh\n")
        continue
    
    computer_choice = random.choice(options)
    print(f"Computer ne chuna: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Draw ho gaya 🤝\n")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Tu jeeta! 🔥\n")
        user_score += 1
    else:
        print("Computer jeeta 😅\n")
        computer_score += 1
