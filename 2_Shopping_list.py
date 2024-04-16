# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list until the user replies "stop", 
# and then returns the shopping list. 

def shopping_list():
    grocery_list=[]
    while True:
        groceries = input("Enter grocery items until complete, which can use 'stop' to end list:")
        if groceries == "stop":
            break
    grocery_list.append(groceries)
    return grocery_list


print("grocery list", grocery_list)


# Task 2: Include a feature to remove items from the list. 
# Task 3: Add a feature that prints out the entire list in a formatted way.