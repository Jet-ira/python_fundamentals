#!/usr/bin/python
"""Create a list to store at least 5 grocery items"""

# Step 1: Create a list with the given grocery items
grocery_list = ["fish", "bread", "milk", "banana", "butter"]

# Step 2: Print the entire list
print("Original grocery list:", grocery_list)

# Step 3: Add a new item to the list
grocery_list.append("bread")
print("After adding bread:", grocery_list)

# Step 4: Remove an item (e.g., "butter")
grocery_list.remove("butter")
print("After removing butter:", grocery_list)

# Step 5: Display the final list using slicing
print("Final list (using slicing):", grocery_list[:])
