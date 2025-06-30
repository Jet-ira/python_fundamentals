#!/urs/bin/python
"""Create a dictionary to act like a phonebook with names as keys and phone numbers as values.
Add at least 3 contacts. Print all keys and values.
Update a contact’s number. Delete a contact."""

phonebook = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012"
}

print("Phonebook entries:")
for name, number in phonebook.items():
    print(f"{name}: {number}")


phonebook["Bob"] = "999-999-9999"
print("\nUpdated Bob's number:")
print(f"Bob: {phonebook['Bob']}")

del phonebook["Alice"]
print("\nDeleted Alice from phonebook.")


print("\nFinal phonebook entries:")
for name, number in phonebook.items():
    print(f"{name}: {number}")
