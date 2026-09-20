#whether the number is prime or not
#if the no. is divisible by any number other than 1 and itself, it is not prime

n = int(input("Enter a number: "))

for i in range(2, n):  
    if(n % i == 0):
        print("The given no. is not prime")
        break
else:
    print("The no. is prime")