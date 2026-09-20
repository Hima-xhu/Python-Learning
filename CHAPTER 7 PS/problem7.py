#star Pattern
'''
    *                          in each column - (n-i) blank spaces at start and odd no. of stars
   ***                                          i.e. (2i-1) stars
  *****

    *
   ***
  *****
 *******
*********

'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(" "* (n-i), end = "")   # end = "" is used to avoid the new line
    print("*"* (2*i - 1))