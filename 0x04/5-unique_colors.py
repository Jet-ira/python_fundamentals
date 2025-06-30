#!/usr/bin/python
"""Create a set that stores colors mentioned by the user (they will enter 5 colors).
Display the set. Try adding a duplicate and show that sets don't allow duplicates.
Show how many unique colors were added."""


# Step 1: Create an empty set
color_set = set()

# Step 2: Get 5 colors from the user
for i in range(5):
    color = input(f"Enter color {i + 1}: ").strip().lower()
    color_set.add(color)

# Step 3: Display the set
print("\nUnique colors entered:", color_set)

# Step 4: Try adding a duplicate color
duplicate_color = next(iter(color_set))  # Pick an existing color to duplicate
color_set.add(duplicate_color)
print(f"\nTried adding duplicate color '{duplicate_color}' again.")

# Step 5: Display the set again (should be unchanged)
print("Set after adding duplicate:", color_set)

# Step 6: Show how many unique colors were added
print("Number of unique colors:", len(color_set))
