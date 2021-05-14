import random
import hangman_words
import hangman_art

print(hangman_art.logo)

end_of_game = False
lives = 6

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

display = []
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Initialize display
for _ in range (word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check if guess is already in display
    if guess in display:
        print("You've already guessed " + guess)
        
    #Check if guessed letter is in chosen_word
    if guess not in chosen_word:
        print("You guessed " + guess + ", that's not in the word. You lose a life.")
        #Reduce numbers of lives
        lives -= 1
    else:
        #Check guessed letter position
        for position in range (word_length):
            if chosen_word[position] == guess:
                display[position] = guess

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    print(hangman_art.stages[lives])
    print(f"Remaining lives: {lives}\n")

    #Validate end of game
    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print ("Game over")
