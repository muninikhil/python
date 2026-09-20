print("learning tuples")
t = (1, 2, 3)
print("The tuple is:", t) #printing the tuple
print("The first element is:", t[0]) #accessing the first element
s=list(t) #converting tuple to list
print("The converted list is:", s) #printing the converted list
s.insert(1, 4) #inserting 4 at index 1
s.append(5) #adding 5 to the end
t = tuple(s) #converting the updated list back to tuple
print("The updated tuple is:", t) #printing the updated tuple


e = (6, 7, 8) #creating another tuple   
print("The second tuple is:", e) #printing the second tuple
t = t + e #concatenating the two tuples
print("The concatenated tuple is:", t) #printing the concatenated tuple 
