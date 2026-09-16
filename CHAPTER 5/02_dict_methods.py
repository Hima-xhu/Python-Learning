marks = {
    "Himanshu" : 100,
    "Prathvi" : 98,      #Key value pairs 
    "Abhinav" : 95,       #Key : value
    "List" : [22, 54, 78],
      0 : "Himanshu"
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Himanshu" : 99, "Vinod Shukla" : 90})
print(marks)

print(marks.get("Himanshu"))  #returns the value of the specifies keys

print(marks.get("Jhanak"))  #returns NONE
print(marks["Jhanak"])   #returns an error