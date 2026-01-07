import random

def hangman():
    
    words = ["apple", "banana", "grapes", "orange", "mango"]

    
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman Game!")
    print("You have 6 incorrect guesses.\n")

    while attempts > 0:
        display_word = ""

        
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word.strip())
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", attempts)

        
        if "_" not in display_word:
            print("\n Congratulations! You guessed the word:", word)
            break

        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")

        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)

        else:
            print("Wrong guess!")
            guessed_letters.append(guess)
            attempts -= 1

        print("-" * 30)

    if attempts == 0:
        print("\n❌  game Over! The word was:", word)


hangman()

