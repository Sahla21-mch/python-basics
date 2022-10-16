# creating an empty list in python
from pickle import POP


Name = []
# adding elements to an empty list 
    #using appemd method
Name.append("Sandrine")
print (Name)
Name.append("John")
Name.append("Edmund")
Name.append("Beri")
print (Name)
    #using insert method
Name.insert(1,"Sandra")
Name.insert(3,"Nestor")
print(Name)

# removing items from a list 
    # using the delete method 
del Name [2]
print(Name)
    #using pop method
Name.pop (2)
print(Name)
Name.pop()
print(Name)
    #using the remove method 
Name.remove("Edmund")
print (Name)

#looping 
for name in Name:
    print(name, " how did you sleep?")
# dealing with numbers in python
numbers = list(range(0,21))
print(numbers)
print(max(numbers))
print(min(numbers))    
print(sum(numbers))

