import random

#Randomly choose a word from the word_list and assing it to a variable
word_list = ["ardvark", "baboon", "camel"]

rnd = random.randint(0, 2)
chosen_word = word_list[rnd] #random.choice(word_lsit) auch möglich

#Testting code
print(f"Psst, the solution is {chosen_word}.")

#create a empty list for each letter in chose_word and add "_" to it.
length = len(chosen_word)
display = []

for i in range(length):
    display.append("_")

#ask the user to guess a letter and assign their answer to a variable. (make it lowercase)
#use a while loop to let the user guess again
if "_" in display:
    while length != 0:
        length = length - 1
        guess = input("Guess a letter: ")# .lower am ende acuh möglich
        guess = guess.lower()

#check if the letter from the inout is correct -> one of the letters form chosen_word
#loop each position in chosen_word and see if letter fits positon than replace it

        letter_list = list(chosen_word)
        a = -1
        for letter in letter_list:
            a = a + 1
            if letter == guess:
                display[a] = guess

        # print display
        print(display)
if length == 0 and "_" in display:
    print("You lost!! ")
elif "_" not in display:
    print("You Won")


