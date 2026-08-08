import random

def main():
    print("--- WELCOME TO THE NUMBER GUESSING GAME ---")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100 inclusive
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Correct! You found the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    main()


import random

def play_round():
    secret_number = random.randint(1, 100)
    attempts_left = 7  # The player has 7 lives
    attempts_taken = 0
    
    print("\nI have picked a new number between 1 and 100.")
    print(f"You have {attempts_left} attempts to guess it!")

    while attempts_left > 0:
        try:
            guess = int(input(f"\n[{attempts_left} attempts left] Enter your guess: "))
            
            # Simple boundary check
            if guess < 1 or guess > 100:
                print("Please stay within the 1 to 100 range.")
                continue
                
            attempts_taken += 1
            attempts_left -= 1
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"🎉 Victory! You guessed the number in {attempts_taken} tries!")
                return attempts_taken  # Return score to check for high score
                
        except ValueError:
            print("Invalid input! Please type a valid number.")

    print(f"\nGame Over! You ran out of attempts. The number was {secret_number}.")
    return None  # No high score if you lose

def main():
    print("--- ULTIMATE NUMBER GUESSING GAME ---")
    high_score = float('inf')  # Set high score to infinity initially (lower is better)

    while True:
        score = play_round()
        
        # Check and update high score
        if score and score < high_score:
            high_score = score
            print(f"🏆 New personal best score: {high_score} attempts!")
        elif high_score != float('inf'):
            print(f"Current High Score to beat: {high_score} attempts.")

        # Ask to replay
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['y', 'yes']:
            print("\nThanks for playing! Final High Score:", "None yet" if high_score == float('inf') else f"{high_score} attempts")
            break

if __name__ == "__main__":
    main()
