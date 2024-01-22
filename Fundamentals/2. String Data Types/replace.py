'''For This task we are working with the replace() & upper() method.
This will let us manipulate the 'pangram' string.
We will then be printing the variable in reverse.
'''

# Store the string "The!quick!brown!fox!jumps!over!the!lazy!dog." as 'pangram'.
# Use the replace() function to swap '!' with blank spaces and overwrite variable.
# Then print the new variable.
# Use the upper() function with print to reprint the sentence in uppercase.
# Use slicing with negative 1 to instruct the string to print in reverse order.

pangram = "The!quick!brown!fox!jumps!over!the!lazy!dog."

pangram = (pangram.replace("!"," "))

print (pangram)
print (pangram.upper())
print (pangram[::-1])