import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        self.window = tk.Tk()
        self.window.title("Guessing Game")

        self.label = tk.Label(self.window, text="I'm thinking of a number between 1 and 100.")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.button.pack()

        self.hint_button = tk.Button(self.window, text="Hint", command=self.show_hint)
        self.hint_button.pack()

        self.menu_button = tk.Button(self.window, text="Main Menu", command=self.return_to_menu)
        self.menu_button.pack()

        self.window.mainloop()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1

        if guess < self.number:
            messagebox.showinfo("Result", "Too low! Try again.")
        elif guess > self.number:
            messagebox.showinfo("Result", "Too high! Try again.")
        else:
            messagebox.showinfo("Result", f"Congratulations! You guessed the number in {self.attempts} attempts!")
            self.window.destroy()

    def show_hint(self):
        if self.attempts >= 7:
            hint = "The number starts with the digit " + str(self.number)[0]
            messagebox.showinfo("Hint", hint)
        else:
            messagebox.showinfo("Hint", "Hint is only available after 7 attempts.")

    def return_to_menu(self):
        self.window.destroy()

class WordJumble:
    def __init__(self):
        self.words = ['python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone']

    def play(self):
        self.window = tk.Tk()
        self.window.title("Word Jumble")

        self.word = random.choice(self.words)
        self.jumbled_word = ''.join(random.sample(self.word, len(self.word)))

        self.label = tk.Label(self.window, text="Unscramble the letters to make a word.")
        self.label.pack()

        self.jumbled_label = tk.Label(self.window, text="Jumbled word: " + self.jumbled_word)
        self.jumbled_label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.button.pack()

        self.menu_button = tk.Button(self.window, text="Main Menu", command=self.return_to_menu)
        self.menu_button.pack()

        self.window.mainloop()

    def check_guess(self):
        guess = self.entry.get()

        if guess == self.word:
            messagebox.showinfo("Result", "Congratulations! You guessed the word correctly!")
        else:
            messagebox.showinfo("Result", "Oops! That's not the correct word.")

        messagebox.showinfo("Word", "The word was: " + self.word)
        self.window.destroy()

    def return_to_menu(self):
        self.window.destroy()

class Hangman:
    def __init__(self):
        self.words = ['python', 'hangman', 'game', 'computer', 'programming']
        self.max_guesses = 6

    def play(self):
        self.window = tk.Tk()
        self.window.title("Hangman")

        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.incorrect_guesses = 0

        self.label = tk.Label(self.window, text="Guess the word by suggesting letters.")
        self.label.pack()

        self.word_label = tk.Label(self.window, text="Word: " + self.get_display_word())
        self.word_label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.button.pack()

        self.menu_button = tk.Button(self.window, text="Main Menu", command=self.return_to_menu)
        self.menu_button.pack()

        self.window.mainloop()

    def get_display_word(self):
        display_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        return display_word

    def check_guess(self):
        guess = self.entry.get().lower()

        if guess in self.guessed_letters:
            messagebox.showinfo("Result", "You already guessed that letter. Try again.")
        else:
            self.guessed_letters.append(guess)

            if guess in self.word:
                messagebox.showinfo("Result", "Correct guess!")
            else:
                self.incorrect_guesses += 1
                messagebox.showinfo("Result", "Incorrect guess!")
                messagebox.showinfo("Guesses", f"You have {self.max_guesses - self.incorrect_guesses} guesses remaining.")

                if self.incorrect_guesses == self.max_guesses:
                    messagebox.showinfo("Game Over", "You ran out of guesses.")
                    messagebox.showinfo("Word", "The word was: " + self.word)

        self.word_label.config(text="Word: " + self.get_display_word())

        if self.get_display_word() == self.word:
            messagebox.showinfo("Result", "Congratulations! You guessed the word correctly!")
            self.window.destroy()

    def return_to_menu(self):
        self.window.destroy()

class NumberMastermind:
    def __init__(self):
        self.number_length = 4
        self.max_attempts = 10

    def play(self):
        self.window = tk.Tk()
        self.window.title("Number Mastermind")

        self.secret_number = self.generate_random_number()
        self.attempts = 0

        self.label = tk.Label(self.window, text=f"Guess the {self.number_length}-digit number.")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.button.pack()

        self.menu_button = tk.Button(self.window, text="Main Menu", command=self.return_to_menu)
        self.menu_button.pack()

        self.window.mainloop()

    def generate_random_number(self):
        return ''.join(random.sample('0123456789', self.number_length))

    def evaluate_guess(self, guess):
        correct_numbers = sum(1 for x, y in zip(self.secret_number, guess) if x == y)
        correct_positions = sum(1 for x, y in zip(self.secret_number, guess) if x == y)
        return correct_numbers, correct_positions

    def check_guess(self):
        guess = self.entry.get()

        if len(guess) != self.number_length or not guess.isdigit():
            messagebox.showinfo("Invalid Input", f"Please enter a {self.number_length}-digit number.")
            return

        self.attempts += 1
        correct_numbers, correct_positions = self.evaluate_guess(guess)

        messagebox.showinfo("Numbers", f"Numbers in the correct position: {correct_positions}")
        messagebox.showinfo("Numbers", f"Numbers in the wrong position: {correct_numbers - correct_positions}")

        if guess == self.secret_number:
            messagebox.showinfo("Result", "Congratulations! You guessed the number correctly!")
            self.window.destroy()

        if self.attempts == self.max_attempts:
            messagebox.showinfo("Game Over", "You reached the maximum number of attempts.")
            messagebox.showinfo("Number", "The secret number was: " + self.secret_number)
            self.window.destroy()

    def return_to_menu(self):
        self.window.destroy()

class MultiGameProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Multi-Game Program")

        self.label = tk.Label(self.window, text="Welcome to the Multi-Game Program!")
        self.label.pack()

        self.button1 = tk.Button(self.window, text="Guessing Game", command=self.play_guessing_game)
        self.button1.pack()

        self.button2 = tk.Button(self.window, text="Word Jumble", command=self.play_word_jumble)
        self.button2.pack()

        self.button3 = tk.Button(self.window, text="Hangman", command=self.play_hangman)
        self.button3.pack()

        self.button4 = tk.Button(self.window, text="Number Mastermind", command=self.play_number_mastermind)
        self.button4.pack()

        self.button5 = tk.Button(self.window, text="Exit", command=self.window.quit)
        self.button5.pack()

        self.window.mainloop()

    def play_guessing_game(self):
        self.window.destroy()
        game = GuessingGame()
        game.play()
        self.window.deiconify()

    def play_word_jumble(self):
        self.window.destroy()
        game = WordJumble()
        game.play()
        self.window.deiconify()

    def play_hangman(self):
        self.window.destroy()
        game = Hangman()
        game.play()
        self.window.deiconify()

    def play_number_mastermind(self):
        self.window.destroy()
        game = NumberMastermind()
        game.play()
        self.window.deiconify()

if __name__ == '__main__':
    program = MultiGameProgram()
