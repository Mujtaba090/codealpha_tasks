import random
import os

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    Fore = Style = type('', (), {'RED': '', 'GREEN': '', 'YELLOW': '', 'CYAN': '', 'RESET_ALL': ''})()

# ASCII hangman stages
hangman_pics = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    words = ["apple", "grape", "mango", "peach", "melon"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    max_attempts = 6
    wrong_attempts = 0

    print(Fore.CYAN + "\n🎯 Welcome to Hangman!")
    print(Fore.YELLOW + "Guess the word by entering one letter at a time.")
    print(Fore.YELLOW + "You can only make 6 incorrect guesses.\n")

    while wrong_attempts < max_attempts and "_" in guessed_word:
        print(hangman_pics[wrong_attempts])
        print("\nWord: " + " ".join(guessed_word))
        print(Fore.YELLOW + f"Guessed letters: {', '.join(guessed_letters)}")
        print(Fore.MAGENTA + f"Attempts left: {max_attempts - wrong_attempts}")

        guess = input(Fore.CYAN + "Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(Fore.RED + "❗ Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print(Fore.RED + "❗ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(Fore.GREEN + "✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(Fore.RED + "❌ Wrong guess.")
            wrong_attempts += 1

        print(Style.RESET_ALL)
    
    clear_screen()
    print(hangman_pics[wrong_attempts])
    if "_" not in guessed_word:
        print(Fore.GREEN + f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(Fore.RED + f"💀 Game Over! The correct word was: {word}")

def main():
    while True:
        clear_screen()
        play_game()
        again = input(Fore.CYAN + "\n🔁 Play again? (y/n): ").strip().lower()
        if again != 'y':
            print(Fore.YELLOW + "Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
