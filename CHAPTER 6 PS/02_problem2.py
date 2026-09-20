marks1 = int(input("Enter marks1: "))
marks2 = int(input("Enter marks2: "))
marks3 = int(input("Enter marks3: "))

totalPercentage = (marks1 + marks2 + marks3)*100 / 300

if(marks1 > 100 or marks2 > 100 or marks3 > 100 or marks1 < 0 or marks2 < 0 or marks3 < 0):
    print("you have entered wrong marks")

else:
    if(totalPercentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
        print("you are passed")

    else:
        print("You are failed")