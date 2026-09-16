a = input("Enter  a number: ")
b = input("enter another number: ")
sum = a + b
print("sum of a and b is :", sum)  #String concatenation will happen because input function takes input as string

c = int(a) + int(b)  #typecasting to integer
print("sum of a and b is : ", c)  #Now addition will happen because we have typecasted the input to integer

d = int(input("enter a number: "))
e = int(input(" enter another number: ")) 
print ("sum of d and e is: ", d+e)  #typecasting to integer in the same line