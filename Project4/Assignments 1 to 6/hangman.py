import random 
def hangman():
    words = ["python","java","coding","krips"]
    word = random.choice(words)
    guessed_word = []
    atempts = 6
    displayed_word = ["_"] * len(word)
    print("Welcome to hangman")
    while atempts > 0 and "_" in displayed_word:
        print("current word:"+ " ".join(displayed_word))
        print(f"attempts left: {atempts}")
        guess = input("guess a letter: ").lower()
        if guess in guessed_word:
            print("You already guessed that letter! Try another one.")
        elif guess in word:
            print("Correct guess! ✅")
            guessed_word.append(guess)
            for index,letter in enumerate(word):
                if letter == guess:
                    displayed_word[index] = letter
        else:
            print("Wrong guess! ❌")
            guessed_word.append(guess)
            atempts -= 1
    if "_" not in displayed_word:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"☠ Game Over! The correct word was: {word}")
        
        
hangman()
        
            
        
        