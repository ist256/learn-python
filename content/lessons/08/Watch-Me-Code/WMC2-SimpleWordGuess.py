name = input("Please enter your name: ")
word = "Python"
guessed_letters = []
trys = 4

while True:
    guess = input("Please enter a guess or a letter ")
    trys = trys - 1
    if len(guess) > 1:
        if guess == word:
            print("You Guessed Correct!")
            break
        else:
            print("You Guessed wrong")
    else:
        guessed_letters.append(guess)
        shown = ""
        for letter in word:
            if letter in guessed_letters:
                shown += letter
            else:
                shown += "_"
        print(shown)
        if trys == 0:
            print("Gave Over!")
            break
    print("You only have %d trys left" % trys)