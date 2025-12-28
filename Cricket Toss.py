import random

name = input("Enter your name: ")

# --- VALIDATION FOR BAT/BOWL ---
while True:
    want = input("Do you want to Bat or Bowl: ").strip().lower()
    if want in ["bat", "bowl"]:
        break
    print("❌ Invalid input. Please type exactly 'Bat' or 'Bowl'.")

# --- VALIDATION FOR STARTING THE GAME ---
while True:
    continue_loop = input("Do you want to play a toss? (y/n): ").strip().lower()
    if continue_loop in ["y", "n"]:
        break
    print("❌ Invalid input. Please enter 'y' or 'n'.")

wins = 0
total_games = 0

while continue_loop == "y":
    try:
        user_choice = int(input("\nEnter your choice (1 for Heads, 2 for Tails): "))

        if user_choice not in [1, 2]:
            print(f"Invalid choice {name}. Please choose either 1 or 2.")
            continue  # This jumps back to the start of the while loop

        total_games += 1
        comp_choice = random.choice([1, 2])

        if comp_choice == 1:
            print("Computer chose: Heads")
        else:
            print("Computer chose: Tails")

        if user_choice == comp_choice:
            print(f"🎉 {name} wins the toss! You can {want.capitalize()}.")
            wins += 1
        else:
            opp_action = "Bowl" if want == "bat" else "Bat"
            print(f"❌ {name} loses the toss! You have to {opp_action}.")

    except ValueError:
        print(f"Invalid input {name}. Please enter a numeric value.")

    # Re-validating the "play again" input
    while True:
        continue_loop = input("\nDo you want to play again? (y/n): ").strip().lower()
        if continue_loop in ["y", "n"]:
            break
        print("Please enter 'y' or 'n'.")

# --- Results Summary ---
print("\n--- Game Summary ---")
print(f"Total Tosses: {total_games}")
print(f"Wins: {wins}")

if total_games > 0:
    luck_percentage = (wins / total_games) * 100
    print(f"Your Luck Factor: {luck_percentage:.2f}%")
else:
    print("No games were played.")

print(f"Goodbye, {name}!")