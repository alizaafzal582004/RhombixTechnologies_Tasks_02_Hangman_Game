import random
import os

# Function to clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function to display the main menu
def display_menu(num_tries, hidden_word, message):
    print("\033[35m", end="")  # Set text color to magenta
    clear_screen()
    print("\t\t\t************************************")
    print("\t\t\t*                                  *")
    print("\t\t\t*          SAVE THE MAN            *")
    print("\t\t\t*                                  *")
    print("\t\t\t************************************")

    print(" \t\t 0 ")
    print(" \t\t/|\\")
    print(" \t\t/ \\")

    print("\t\t==========================================")
    print(f"\n\t\tYou have {num_tries} tries to guess the word.")
    print(f"\n\n\t\t\t\t{message}")
    print("\t\t==========================================")
    print("\033[0m", end="")  # Reset text color

# Function to check the guessed letter
def check_guess(secret_word, hidden_word, guess):
    matches = 0
    for i in range(len(secret_word)):
        if guess == hidden_word[i]:
            return 0  # already guessed
        if guess == secret_word[i]:
            hidden_word[i] = guess
            matches += 1
    return matches

# Function to save the results to a file
def save_results_to_file(category, secret_word, is_win):
    try:
        with open("Result.hangman.txt", "a") as result_file:
            result_file.write(f"Category: {category}\n")
            result_file.write(f"Secret Word: {secret_word}\n")
            result_file.write(f"Result: {'Win' if is_win else 'Loss'}\n")
            result_file.write("-----------------------------------\n")
    except:
        print("Error: Unable to open file Result.hangman.txt")

# Function to play the game
def play_game(secret_word, category, is_easy_level):
    num_tries = 3
    hidden_word = ["-"] * len(secret_word)
    message = "Play!"
    is_win = False

    # Reveal first letter in easy mode
    if is_easy_level:
        hidden_word[0] = secret_word[0]

    while num_tries > 0:
        display_menu(num_tries, "".join(hidden_word), message)
        print("\n\t\t\t\t" + "".join(hidden_word))
        letter = input("\n\n\t\t\t\tGuess a letter: ").lower()

        if check_guess(secret_word, hidden_word, letter) == 0:
            message = "Incorrect letter."
            num_tries -= 1
        else:
            message = "NICE! You guessed a letter."

        if "".join(hidden_word) == secret_word:
            message = "Congratulations! You got it. Man has been saved!"
            is_win = True
            display_menu(num_tries, "".join(hidden_word), message)
            print("\\ 0 / ")
            print("  |")
            print(" / \\")
            print("\t\t==========================================")
            print(f"\n\t\t\tThe word is : {secret_word}")
            print("\t\t\t\t                                      ")
            print("\t\t==========================================")
            break

    if num_tries == 0:
        message = "NOOOOOOO!...Man has been hanged."
        display_menu(num_tries, "".join(hidden_word), message)
        print("   _____")
        print("  |     |")
        print("  |     O")
        print("  |    /|\\")
        print("  |    / \\")
        print("  |")
        print("  |")
        print(" _|___ ")
        print("\t\t==========================================")
        print(f"\n\t\t\tThe word was : {secret_word}")
        print("\t\t\t\t                                      ")
        print("\t\t==========================================")

    save_results_to_file(category, secret_word, is_win)

# Function to get random word
def get_random_word(words):
    if not words:
        return ""
    return random.choice(words)

def main():
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    fruits = [
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
        "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange",
        "papaya", "quince", "raspberry", "strawberry", "tangerine",
        "blueberry", "watermelon"
    ]
    animals = [
        "antelope", "buffalo", "cheetah", "dolphin", "elephant", "flamingo",
        "giraffe", "hippopotamus", "iguana", "jaguar", "kangaroo", "lemur",
        "mongoose", "narwhal", "octopus", "penguin", "quokka", "rhinoceros",
        "salamander", "tiger"
    ]

    print("\t\t\t\t************************************")
    print("\t\t\t\t*                                  *")
    print("\t\t\t\t*      WELCOME TO HANGMAN GAME     *")
    print("\t\t\t\t*                                  *")
    print("\t\t\t\t************************************")
    print("\t\t\t\t                                  ")
    
    print(" \t\t\t 0 ")
    print(" \t\t\t/|\\")
    print(" \t\t\t/ \\")
    print("\n\t\t\t****************************************")

    print("\n\t\t\t\t      SELECT A CATEGORY: ")
    print("\t\t\t\t                                  ")
    print("\n\t\t\t\t     1. MONTHS")
    print("\n\t\t\t\t     2. FRUITS ")
    print("\n\t\t\t\t     3. ANIMALS ")
    print("\t\t\t\t                                  ")
    print("\n\t\t\t****************************************")

    category_choice = int(input("\n\t\t\t\t      Enter your choice: "))

    words = []
    category_name = ""
    if category_choice == 1:
        words = months
        category_name = "MONTHS"
    elif category_choice == 2:
        words = fruits
        category_name = "FRUITS"
    elif category_choice == 3:
        words = animals
        category_name = "ANIMALS"
    else:
        print("Invalid category. Defaulting to months.")
        words = months
        category_name = "MONTHS"

    clear_screen()
    print("\t\t\t\t*******************************")
    print("\t\t\t\t*                             *")
    print("\t\t\t\t* Select Difficulty Level     *")
    print("\t\t\t\t*                             *")
    print("\t\t\t\t*******************************")
    print("\t\t\t\t                                  ")
    
    print(" \t\t\t 0 ")
    print(" \t\t\t/|\\")
    print(" \t\t\t/ \\")
    print("\n\t\t\t**************************************")
    print("\t\t\t\t                                  ")
    print("\n\t\t\t\t1. Easy Level ")
    print("\n\t\t\t\t2. Hard Level ")
    print("\t\t\t\t                                  ")
    print("\n\t\t\t*************************************")
    print("\t\t\t\t                                  ")
    level = int(input("\n\t\t\t\tEnter your choice: "))
    is_easy_level = (level == 1)

    random.seed()
    secret_word = get_random_word(words)

    if not secret_word:
        print("No words available. Exiting game.")
        return

    play_game(secret_word, category_name, is_easy_level)

if __name__ == "__main__":
    main()
