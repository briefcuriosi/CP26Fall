import random

word = ["spook", "halloween", "pumpkin"]
target = random.choice(word)
print(target)

progress = ['-'] * len(target)
print(*progress)

while True:
    guess = input("Enter a character :")
    print(guess)
    if guess not in target:
     print( "Wrong guess! Try again")
    else:
        for i in range (len(target)):
            if target[i] == guess:
                progress[i] = guess
    print(*progress)
    print()