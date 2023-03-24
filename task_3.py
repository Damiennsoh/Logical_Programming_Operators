# Design a program that determines the award a person competing in a triathlon will receive.
# Below are my pseudocode steps as I will be following these steps to write my program in order to dispens the awards according to the award table and it's corresponding time of the three events.

# creating an event input for all three events- thus swimming, cycling and running
running = int(input("what is the time taken for swimming in minutes ? Enter it here: ")) # Here, the input function input() is by default a string, but because I'm dealing with time which is an int, I first of all need to cast the data type from string into an int. That is why the int data type is placed infront of the input function.
print("Time taken for running in minutes is: ", running)

cycling = int(input("Enter the time taken for cycling in minutes here: "))
print("Time taken for cycline in minutes is ", cycling)

swimming = int(input("Enter the time taken for swimming in minutes here: "))
print("The time taken for swimmming in minutes is: ", swimming)

# It also means I will have to add the total time taken by each of the three events.
Total_Triathlon_Time = running + swimming + cycling
print("Total triathlon time taken is: ", Total_Triathlon_Time, "minutes")

# I then need to compare the combined total time of each of the three events with the award table provided.
# The time in question is in minutes.
# After comparing the total time taken by the three events with the award table, I can then print out my awards statements based on 
# the combined time of the three events and what award it corresponds to.
# I will be using my if statements to control the flow of the program as well as my decisions.
#
