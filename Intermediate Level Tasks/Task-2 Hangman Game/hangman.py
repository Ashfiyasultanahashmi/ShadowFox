import random

def display_hangman(wrong_guesses):
    stages = [
        """
          -----
          |   |
              |
              |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
              |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
          |   |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|   |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         /    |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        --------
        """,
    ]
    return stages[wrong_guesses]

def play_hangman():
    word_hint_pairs = [
        ("hijab", "A headscarf worn by Muslim women."),
        ("abaya", "A loose-fitting robe often worn by Muslim women."),
        ("eid", "A festival celebrated after Ramadan."),
        ("quran", "The holy book of Islam."),
        ("tasbih", "A string of beads used for prayer and remembrance."),
        ("mehndi", "Henna designs applied during special occasions."),
        ("muslimah", "A Muslim woman."),
        ("burqa", "A full-body covering worn by some Muslim women."),
        ("kaaba", "The holy site in Mecca that Muslims face during prayer."),
        ("noor", "A name meaning 'light' in Arabic."),
    ]

    word, hint = random.choice(word_hint_pairs)
    guessed = set()
    mistakes = 0
    max_mistakes = 6

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")

    while mistakes < max_mistakes:
        print(display_hangman(mistakes))
        word_progress = [char if char in guessed else "_" for char in word]
        print("Current Word: " + " ".join(word_progress))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please type a single letter.")
            continue

        if guess in guessed:
            print(f"You've already guessed '{guess}'. Try something new.")
        elif guess in word:
            print(f"Nice! The letter '{guess}' is in the word.")
            guessed.add(guess)
        else:
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
            guessed.add(guess)
            mistakes += 1

        if all(char in guessed for char in word):
            print("Congratulations! You've guessed the word!")
            print(f"The word was: {word}")
            break
    else:
        print(display_hangman(mistakes))
        print("You've run out of guesses! Game Over.")
        print(f"The word was: {word}")

play_hangman()
