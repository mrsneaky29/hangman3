import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
stages = hangman_art.stages

lives = 6

print(hangman_art.logo)


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    guessed_letters = []
    guessed_letters.append(guess)
    
    if guess in guessed_letters:
        print("You already guessed that letter." + guess)
        if guess in correct_letters:
            print(f"You already guessed " + {guess})

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print("You guessed " + guess + " It was wrong and you lose a life.")

        if lives == 0:
            game_over = True
            print(f"*********************** The word was {chosen_word}! YOU LOSE**********************")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
