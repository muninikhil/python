dictnory={"name":"nikhil","age":22,"city":"banglore"}
print(dictnory)
remove={"age":22}
for key in remove:
    if key in dictnory:
        del dictnory[key]
print(dictnory)
add={"country":"india"}
dictnory.update(add)
print(dictnory)
pop_item=dictnory.pop("city")
print(dictnory)
print("Popped item:", pop_item)
print("Keys in the dictionary:", list(dictnory.keys()))
print("Values in the dictionary:", list(dictnory.values()))
print("Items in the dictionary:", list(dictnory.items()))