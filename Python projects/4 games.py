import random
            #number guessing game
def guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

        if attempts == 7:
            hint = "The number starts with the digit " + str(number)[0]
            print("Hint:", hint)

    print("Thank you for playing!")

            #word jumble
def word_jumble():
    words = ['python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone']
    word = random.choice(words)
    jumbled_word = ''.join(random.sample(word, len(word)))

    print("Welcome to Word Jumble!")
    print("Unscramble the letters to make a word.")
    print("Jumbled word:", jumbled_word)

    guess = input("Your guess: ")

    if guess == word:
        print("Congratulations! You guessed the word correctly!")
    else:
        print("Oops! That's not the correct word.")

    print("The word was:", word)
    print("Thank you for playing!")
    
        #hangman
        
def hangman():
    words = ['python', 'hangman', 'game', 'computer', 'programming']
    word = random.choice(words)
    guessed_letters = []
    max_guesses = 6
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print("Guess the word by suggesting letters.")

    while True:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("Word:", display_word)

        if display_word == word:
            print("Congratulations! You guessed the word correctly!")
            break

        guess = input("Your guess: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            guessed_letters.append(guess)

            if guess in word:
                print("Correct guess!")
            else:
                incorrect_guesses += 1
                print("Incorrect guess!")
                print(f"You have {max_guesses - incorrect_guesses} guesses remaining.")

                if incorrect_guesses == max_guesses:
                    print("Game over! You ran out of guesses.")
                    print("The word was:", word)
                    break

    print("Thank you for playing!")

                #number_mastermind

def number_mastermind():
    number_length = 4
    max_attempts = 10

    def generate_randoms_number():
        return ''.join(random.sample('0123456789', number_length))

    def evaluate_guess(secret_number, guess):
        correct_numbers = sum(1 for x, y in zip(secret_number, guess) if x == y)
        correct_positions = sum(1 for x, y in zip(secret_number, guess) if x == y)
        return correct_numbers, correct_positions

    secret_number = generate_random_number()
    attempts = 0

    print("Welcome to Number Mastermind!")
    print(f"Guess the {number_length}-digit number.")
    print(f"You have {max_attempts} attempts.")

    while True:
        guess = input("Your guess: ")

        if len(guess) != number_length or not guess.isdigit():
            print(f"Please enter a {number_length}-digit number.")
            continue

        attempts += 1
        correct_numbers, correct_positions = evaluate_guess(secret_number, guess)

        print(f"Numbers in the correct position: {correct_positions}")
        print(f"Numbers in the wrong position: {correct_numbers - correct_positions}")

        if guess == secret_number:
            print("Congratulations! You guessed the number correctly!")
            break

        if attempts == max_attempts:
            print("Game over! You reached the maximum number of attempts.")
            print("The secret number was:", secret_number)
            break

    print("Thank you for playing!")

# Main program
print("Welcome to the Multi-Game Program!")
print("Choose a game to play:")
print("1. Guessing Game")
print("2. Word Jumble")
print("3. Hangman")
print("4. Number Mastermind")

choice = input("Enter the number of the game you want to play: ")

if choice == "1":
    guessing_game()
elif choice == "2":
    word_jumble()
elif choice == "3":
    hangman()
elif choice == "4":
    number_mastermind()
else:
    print("Invalid choice. Exiting the program.")
