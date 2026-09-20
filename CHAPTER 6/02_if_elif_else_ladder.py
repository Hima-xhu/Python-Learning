a = int(input("Enter your age: "))

# if elif else ladder:

if(a>= 18):
    print("you are above age of consent")
    print("Good for you")

elif(a<0):
    print("you are entering an invalid negative age")

elif(a==0):
    print("The value you entered is not accepatable")    

else:
    print("you are below the age of consent")


print("End of program")
