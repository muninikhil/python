cars=["Toyota", "Honda", "Ford"]
cars.append("Chevrolet")
print("The list of cars is:", cars) #printing the list of cars
cars.count("Honda") #counting the occurrences of "Honda" in the list
print("The count of 'Honda' in the list is:", cars.count("Honda")) #printing the count of "Honda" in the list
cars.extend(["Nissan", "Mazda"]) #extending the list with another list
print("The list of cars after extending is:", cars) #printing the list of cars after extending
cars.index("Ford") #finding the index of "Ford" in the list
print("The index of 'Ford' in the list is:", cars.index("Ford")) #printing the index of "Ford" in the list
cars.insert(2, "Subaru") #inserting "Subaru" at index 2
print("The list of cars after inserting 'Subaru' is:", cars) #printing the  
cars.pop(3) #removing the element at index 3
print("The list of cars after popping the element at index 3 is:", cars) #
cars.remove("Toyota") #removing "Toyota" from the list  
cars.reverse() #reversing the list
print("The list of cars after reversing is:", cars) #printing the list of cars after
cars.sort() #sorting the list
print("The list of cars after sorting is:", cars) #printing the list of cars after  
cars.clear() #clearing the list
print("The list of cars after clearing is:", cars) #printing the list of cars after