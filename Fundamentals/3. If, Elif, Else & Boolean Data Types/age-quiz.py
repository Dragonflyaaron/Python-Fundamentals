'''
For this task, using if,elif,else statements,
we are creating an age quiz to output a variety of different
answers depending on the users input.
'''

# Collect users age.
age = input("\nHow old are you? ")

# Store the age as an integer.
age = int(age)

# Starting with highest, can also start with lowest.
if age >= 100: 
    # Print if equal to greater than.
    print ("Sorry you're dead.") 


elif age >= 65: 
    # Print if equal to or greater but less than 100.
    print ("Congrats on your retirement!")


elif age >= 40:
    # Print if equal or greater to but less than 65.
    print ("You're over the hill") 

elif age == 21:
    # Print only if exactly 21.
    print ("Congrats on your 21st!") 

elif age < 13:
    # Print if less than 13 only.
    print ("You qualify for the kiddie discount") 

else:
    # Print for every other number.
    print ("Age is but a number") 