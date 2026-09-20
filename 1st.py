print("Hello, World!")
# Create a list
list1 = [1, 2, 3, 4, 5]
print("The list is:", list1)
print("The length of the list is:", len(list1)) #lengt of list
print("list type is:", type(list1)) #type of list items
print(list1[2:4])  # Slicing the list from index 2 to 4 (exclusive)
if 3 in list1:
    print("3 is present in the list") #checking if 3 is present in the list

list1[1]= 10 # Modifying the second element of the list
print("The modified list is:", list1) #printing the modified list1
list1.insert(2, 15) # Inserting 15 at index 2
print("The list after insertion is:", list1) #printing the list after insertion
list1.append(20) # Appending 20 to the end of the list
print("The list after appending is:", list1) #printing the list after appending
list2 = [6, 7, 8] # Creating another list
list1.extend(list2) # Extending list1 with list2
print("The list after extending is:", list1) #printing the list after extending
list1.remove(10) # Removing the first occurrence of 10 from the list
print("The list after removing 10 is:", list1) #printing the list after removing
del list1[0] # Deleting the first element of the list
print("The list after deleting the first element is:", list1) #printing the list after deleting the first element
cleared_list = list1.clear() # Clearing all elements from the list
print("The list after clearing is:", list1) #printing the list after clearing
list2.pop(2) # Popping the element at index 2 from the list
print("The list after popping is:", list2) #printing the list after popping
