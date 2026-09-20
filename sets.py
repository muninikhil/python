print("learning sets")
sets = {1, 2, 3, 4, 5} #creating a set
print("The set is:", sets) #printing the set
sets.add(6) #adding 6 to the set
print("The set after adding 6 is:", sets) #printing the set after adding
ets={3, 4, 5, 6, 7} #creating another set
print("The second set is:", ets) #printing the second set
sets.update(ets) #updating the first set with the second set
print("The set after updating is:", sets) #printing the set after updating
sets.remove(2) #removing 2 from the set
print("The set after removing 2 is:", sets) #printing the set after removing
sets.union(ets) #union of two sets
print("The union of the two sets is:", sets.union(ets)) #printing the union