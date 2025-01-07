'''
This program contains if statements to show us how python flow control
statements work
'''

# Ask the User for name and age
name = input("What is your name: ")
age = int(input("How old are you: "))

# check for conditions using if statements
if name == "Alice":
    print("Hi Alice")
# if there are other conditions to check we use elif
elif age < 15:
        print('You are not Alice, Kiddo')
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire")
elif age > 100:
    print("You're not Alice, Grannie")
# if name is not Alice then do this
else:
    print("Hello Stranger")