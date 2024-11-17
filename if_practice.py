# Exercise 1

# This bulk of code here introduces the user to the program
# then asks the user for two options
print("Welcome,\n This program gives information about your age and much more options!")
print("To use our program, input your name in the following input:")
name = str(input("Please enter your name: "))
print(f"Great, {name}!\nNow, please choose between two options:\n\n1. A simple program that tells you the age group based on your age.\n2. A program that estimates when you might die based on different factors.")

# Get the user's choice
choice = int(input("Please enter your choice (1 or 2): "))

if choice == 1:  # Option 1
    print("This program will tell you what age group you're in based on your age.")

    # Get the user's input and convert it to an integer
    age = int(input("Please enter your age: "))

    # Check the age and print the appropriate message
    if age < 13:
        print("You are a child.")
    elif age >= 13 and age <= 17:
        print("You are a teenager.")
    elif age >= 18 and age <= 59:
        print("You are an adult.")
    else:
        print("You are an elderly.")

elif choice == 2:  # Option 2
    print("This program will estimate when you might die based on different factors.")
    # You can add functionality for this option here
    # For example, you could ask the user for their lifestyle choices, etc.
    
else:
    print("Invalid choice. Please select either 1 or 2.")
