'''
For this task I needed to create a program that determines an award for persons competeing in a triathalon.
The programe reads in the times in minutes for each event. 
It then calcualtes the total time taken and displays the relevant information back.
'''

# Create a variable for the three sections of the triathlon and save as integer.
# Create a variable to save the total sum of the tree sports added together.
# Make use of an if block to determine the award of the participant and display information back to them.

# Creating our variables and storing as integer.
swimming = int(input("\nHow many minutes did the swimming portion of the triathlon take you?\n")) 

cycling = int(input("How many minutes did the cycling portion of the triathlon take you?\n"))

running = int(input("How many minutes did the running portion of the triathlon take you?\n"))

# Creating a variable to save the total sum of our activites.
score = swimming + cycling + running 

# Starting with the highest number and working in descending order.
# Utilising the greater than or equal to sign.
if score >= 111: 
    # Print the total time and award back to the participant.
    print (f"""\nYou completed the Triathlon in {score} minutes. 
You have not qualified for an award.\n""") 

elif score >= 106:
    print (f"""You have completed the Triathlon in {score} minutes. 
You have been awarded the Provincial Scroll""")

elif score >= 101:
    print (f"""You have completed the Triathlon in {score} minutes. 
You have been awarded the Provincial Half Colours""")

else:
    print (f"""You have completed the Triathlon in {score} minutes. 
You have been awarded the Provinical Colours""")