#Objective: The aim of this assignment is to create a program that helps users make a shopping list.
#Task 1: Write a function that lets the user add items to a list.
def add(list, item): #use .append in a function to add items to the list
    list.append(item)
    return list

#Task 2: Include a function to remove items from the list.
def remove(list, item): #use .remove in a function to remove items from the list
    list.remove(item)
    return list

#Task 3: Add a function that prints out the entire list in a formatted way.
def print_list(list): #use a for range(len()) to print each item in the list on a new line
    print ("Here's your list:")
    for i in range(len(list)):
        print(list[i])
        i += 1

shopping_list = []

print ("This program allows you to manage and view your shopping list!")

while True:
    user_request = input("Would you like to do with your list?(add/remove/print):\n*Type 'quit' to exit* ").lower
    if user_request() == "quit":
        break
    elif user_request() == "add":
        new_item = input("What would you like to add? ")
        add(shopping_list,new_item)
    elif user_request() == "remove":
        item_to_be_removed = input("What would you like to remove? ")
        remove(shopping_list,item_to_be_removed)
    elif user_request() == "print":
        print_list(shopping_list)
    else:
        print("User response not registered. Please input enter one of the following:\nprint, add, remove, or quit")
#use a while true loop to create a infinite loop and use a "quit" option to provide easy exit from the list
#Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.