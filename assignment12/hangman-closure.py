def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        nonlocal guesses
        if letter not in guesses:
            guesses.append(letter)

        display = ''.join([char if char in guesses else '_' for char in secret_word])
        print(display)

        return display == secret_word

    return hangman_closure


if __name__ == "__main__":
    secret = "happiness"
    game = make_hangman(secret)

    print("Let's play Hangman! (The secret word has been set.)\n")

    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if game(guess):
            print("Congratulations! You guessed the word!")
            break