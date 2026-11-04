import random

words = ["spook", "halloween", "pumpkin", "manager", "seat", "campus", "coffee", "reception","safety" ]
target = random.choice(words)

progress = ["_"] * len(target)
wrong_guesses = 0
maximum_wrong_guesses = 6
guessed_letters = []
wrong = 0

print("welcome to hangman!")
print(*progress)

while True:
    guess = input("Enter a character: ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter")
        continue

    if len(guess) !=1 or not guess.isalpha():
        print("you already guess that letter.")
        continue
    guessed_letters.append(guess)

    if guess not in target:
        wrong_guesses += 1
        print("Wrong guesses !")
        print("Wrong guesses:", wrong_guesses,"out of", maximum_wrong_guesses)
    else:
        for i in range(len(target)):
            if target [i] == guess:
                progress[i] = guess
    print(*progress)

    if wrong_guesses >= maximum_wrong_guesses:
        print("Game over! The word was:", target)
        break
    if "_" not in progress:
        print("You won ! The word was", target)
        break
    if wrong ==6:
        print("You lose! The word was ", target)
        break