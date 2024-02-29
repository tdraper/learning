numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.
 
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.

print("\nLength of list: ", len(numbers))

del numbers[1:3]

print("\nNew Length list:", len(numbers))
print("New list contents:", numbers)  # Printing current list contents.
