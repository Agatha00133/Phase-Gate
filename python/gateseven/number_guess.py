import random
def play_game():
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    won = False

    print(" Welcome to the Guessing Game!")
    print("Guess a number between 1 and 100")


def get_rating(attempts, won):
    if not won:
        return "Better luck"
    if attempts == 1:
        return "Legendary"
    elif attempts == 2:
        return "Excellent"
    elif attempts in [3, 4]:
        return "Good"
    elif attempts == 5:
        return "Close!"

 while attempts < max_attempts
        user_input = input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: ")

 
        if not user_input.isdigit():
            print(" Invalid input! Please enter a number.")
            continue
         guess = int(user_input)

        
        if guess < 1 or guess > 100:
            print(" Number must be between 1 and 100.")
            continue
            attempts += 1

        if guess == number:
            print(" Correct! You guessed the number!")
            won = True
            break
        elif guess < number:
            print("Too low! Try a higher number.")
        else:
            print(" Too high! Try a lower number.")

print("\n===== Game Over =====")
print(f"Correct number: {number}")
print(f"Attempts used: {attempts}")
print(f"Rating: {get_rating(attempts, won)}")
