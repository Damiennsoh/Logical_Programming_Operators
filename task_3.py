# Design a program that determines the award a person competing in a triathlon will receive.
# Below are my pseudocode steps as I will be following these steps to write my program in order to dispense the awards according to the award table and it's corresponding time of the three events.

# creating an event input for all three events- thus swimming, cycling and running
running = int(input("what is the time taken for swimming in minutes ? Enter it here: ")) # Here, the input function input() is by default a string, but because I'm dealing with time which is an int, I first of all need to cast the data type from string into an int. That is why the int data type is placed infront of the input function.
print("Time taken for running in minutes is: ", running)

cycling = int(input("Enter the time taken for cycling in minutes here: "))
print("Time taken for cycling in minutes is ", cycling)

swimming = int(input("Enter the time taken for swimming in minutes here: "))
print("The time taken for swimming in minutes is: ", swimming)

# It also means I will have to add the total time taken by each of the three events.
Total_Triathlon_Time = running + swimming + cycling
print("Total triathlon time taken is: ", Total_Triathlon_Time, "minutes")

# Defining the total triathlon time and what it means with regards to the awards
# Within qualifying time = 100 minutes = Provincial Colors
# Within 5 minutes of qualifying time  = 100+5 = 105 minutes = Provincial Half Colors
# Within 10 minutes of qualifying time = 100+10 110 minutes = Provincial Scroll
# More than 10 minutes of qualifying time  = 100+ above 10 minutes. = No award

# Using if-elif-else statements to make decisions for my program.
if Total_Triathlon_Time <= 100:
    print("Provincial Colors Award")
elif (Total_Triathlon_Time > 100 and Total_Triathlon_Time <= 105):
    print("Provincial Half Colors Awards")
elif (Total_Triathlon_Time > 105 and Total_Triathlon_Time <= 110):
    print("Provincial Scroll Awards")
else:
    print("No Award")
