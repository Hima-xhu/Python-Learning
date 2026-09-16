friends = ["Vinod shukla", "Prathvi", "Abhinav" , 3 , False , 2322]
#lists are mutable

#methods

friends.append(32) #add the entered value at the end of list
print(friends)

l1 = [53, 55, 87, 11, 12, 10, 2 ]
l1.sort()

print(l1)

l1.reverse()
print(l1)

l1.insert(2 , 23465) #insert 23465 at index 2
print(l1)

l1.pop(2) #delete the element and return it
print(l1)
print(l1.pop(2))  #print the return value 

l1.remove(11) #remove element 11 from the list
print(l1)