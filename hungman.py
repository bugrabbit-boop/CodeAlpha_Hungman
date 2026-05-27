import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------
# WORD LIST
# -----------------------------
words = ["python", "apple", "chair", "tiger", "music"]

secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Hint letter
hint_letter = random.choice(secret_word)
guessed_letters.append(hint_letter)

# -----------------------------
# WINDOW
# -----------------------------
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x500")
root.config(bg="#1e293b")

# -----------------------------
# TITLE
# -----------------------------
title = tk.Label(
    root,
    text="🎮 Hangman Game",
    font=("Arial", 24, "bold"),
    bg="#1e293b",
    fg="white"
)
title.pack(pady=20)

# -----------------------------
# HINT
# -----------------------------
hint = tk.Label(
    root,
    text=f"💡 Hint Letter: {hint_letter}",
    font=("Arial", 16),
    bg="#1e293b",
    fg="#38bdf8"
)
hint.pack()

# -----------------------------
# WORD DISPLAY
# -----------------------------
word_label = tk.Label(
    root,
    text="",
    font=("Arial", 30, "bold"),
    bg="#1e293b",
    fg="#22c55e"
)
word_label.pack(pady=30)

# -----------------------------
# STATUS
# -----------------------------
status_label = tk.Label(
    root,
    text="Start Guessing!",
    font=("Arial", 14),
    bg="#1e293b",
    fg="white"
)
status_label.pack()

# -----------------------------
# ENTRY BOX
# -----------------------------
guess_entry = tk.Entry(
    root,
    font=("Arial", 20),
    width=5,
    justify="center"
)
guess_entry.pack(pady=20)

# -----------------------------
# UPDATE DISPLAY
# -----------------------------
def update_word():

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    word_label.config(text=display_word)

    # Win condition
    if "_" not in display_word:
        messagebox.showinfo(
            "Winner",
            f"🎉 You guessed the word: {secret_word}"
        )
        root.quit()

# -----------------------------
# CHECK GUESS
# -----------------------------
def check_guess():

    global incorrect_guesses

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        status_label.config(text="⚠ Enter one valid letter")
        return

    # Already guessed
    if guess in guessed_letters:
        status_label.config(text="⚠ Already guessed")
        return

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        status_label.config(text="✅ Correct Guess!")
    else:
        incorrect_guesses += 1
        remaining = max_guesses - incorrect_guesses

        status_label.config(
            text=f"❌ Wrong Guess! Remaining: {remaining}"
        )

    update_word()

    # Lose condition
    if incorrect_guesses == max_guesses:
        messagebox.showerror(
            "Game Over",
            f"💀 The word was: {secret_word}"
        )
        root.quit()

# -----------------------------
# BUTTON
# -----------------------------
guess_button = tk.Button(
    root,
    text="Guess",
    font=("Arial", 16, "bold"),
    bg="#38bdf8",
    fg="black",
    padx=20,
    pady=10,
    command=check_guess
)

guess_button.pack(pady=20)

# -----------------------------
# INITIAL DISPLAY
# -----------------------------
update_word()

# -----------------------------
# MAIN LOOP
# -----------------------------
root.mainloop()