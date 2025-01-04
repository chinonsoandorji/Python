'''
This python program builds a guessing game
'''

'''
secret_word = "giraffe"
guess = ""
while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!")
'''

'''Improvement: lets set a limit to how many times a user can guess
    for instance if the number of trial time is set to 3.
    if they don't get in 3 trials they lose the game
    but if they get on or before 3 trials they win!
'''
"set the variable that stores the secret word"
secret_word = "giraffe"

"This variable stores the users response"
guess = ""

"Tell the user what this games does"
print("Hello ! ")
print("This game lets you guess what the secret word is")
"The while loop runs a prompt until the user gets the word"
while guess != secret_word:
    print("Hint: I am an animal with long neck")
    guess = input("Enter guess: ")

print("You win!")
