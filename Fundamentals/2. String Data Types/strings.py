'''For This task we are working with the strip() method.
This will let us manipulate the 'hero' string
'''

# Create a variable named hero to store "$$$Superman$$$".
# Overwrite the existing variable whilst using the strip() method on '$'s.
# Print the new variable.

hero = "$$$Superman$$$"
hero = (hero.strip('$'))

print (f"\n{hero}\n")
