'''
Now You Code 4: Shopping List

Write a simple shopping list program. 

The main program loop has a menu allowing you to 1) add to the list 2) remove an item from the list or 3) print the list

Example Run

A - Add Item to Shopping List
P - Print Shopping List
R - Remove Item from Shopping List
Q - Quit Shopping List Program
Enter choice: a
Enter Item to Add: eggs
A - Add Item to Shopping List
P - Print Shopping List
R - Remove Item from Shopping List
Q - Quit Shopping List Program
Enter choice: a
Enter Item to Add: eggs
eggs is already in the list!
A - Add Item to Shopping List
P - Print Shopping List
R - Remove Item from Shopping List
Q - Quit Shopping List Program
Enter choice: p
Your List: ['eggs']
A - Add Item to Shopping List
P - Print Shopping List
R - Remove Item from Shopping List
Q - Quit Shopping List Program
Enter choice: r
Enter Item to Remove from List: peas
peas is not in the list!
A - Add Item to Shopping List
P - Print Shopping List
R - Remove Item from Shopping List
Q - Quit Shopping List Program
Enter choice: r
Enter Item to Remove from List: eggs
A - Add Item to Shopping List
P - Print Shopping List
R - Remove Item from Shopping List
Q - Quit Shopping List Program
Enter choice: p
Your List: []
A - Add Item to Shopping List
P - Print Shopping List
R - Remove Item from Shopping List
Q - Quit Shopping List Program
Enter choice: q


Most of the code has been written for you fill in the areas below.
'''

# TODO: Write Todo lists for

# Add item to list if it does not exist

# Remove item from list when it does not exist


# Write code here
def print_menu():
    print("A - Add Item to Shopping List")
    print("P - Print Shopping List")
    print("R - Remove Item from Shopping List")
    print("Q - Quit Shopping List Program")
    return

# prompts for a new item then adds it to the shopping list
# only when it does not exist
# input: shopping list
# output: shopping list
def add_item(shopping_list):
    #todo write code here

    return shopping_list

# sorts then prints the shopping list
# input: shopping list
# output: shopping list
def print_list(shopping_list):
    #todo write code here

    return shopping_list

# prompts for an item then removes it from the shopping list
# only when it exists
# input: shopping list
# output: shopping list
def remove_item(shopping_list):
    #todo write code here

    return shopping_list        


## Main Program Written For You
shopping_list = []
while True:
    print_menu()
    choice = input("Enter choice: ").upper()
    if choice == 'A':
        shopping_list = add_item(shopping_list)
    elif choice == 'P':
        shopping_list = print_list(shopping_list)
    elif choice == 'R':
        shopping_list = remove_item(shopping_list)
    elif choice == "Q":
        break
    else:
        print('ERROR:', choice,'is not a menu option')
