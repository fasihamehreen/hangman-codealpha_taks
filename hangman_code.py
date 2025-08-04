import random

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "program", "computer", "keyboard"]
    
    # Select a random word
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6
    word_progress = ["_"] * len(secret_word)
    
    print("Welcome to Hangman!")
    print(" ".join(word_progress))
    
    while True:
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print("Correct!")
            # Update word progress
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    word_progress[i] = guess
        else:
            attempts_left -= 1
            print(f"Wrong! You have {attempts_left} attempts left.")
            
        # Display current progress
        print(" ".join(word_progress))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Check win/lose conditions
        if "_" not in word_progress:
            print("Congratulations! You won!")
            break
            
        if attempts_left == 0:
            print(f"Game over! The word was: {secret_word}")
            break

# Start the game
hangman()