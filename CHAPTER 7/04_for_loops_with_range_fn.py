# range() function generates a sequence of numbers starting from 0 (by default) and increments by 1 (by default),
# and stops before a specified number.

for i in range(4):     # or for i in range(0, 4):
    print(i)           #prints 0 to 3

# we can also specify the start, stop, and stepsize in the range() function

for i in range(1, 10, 2): #starts from 1, stops before 10, and increments by 2
    print(i)              #prints 1, 3, 5, 7, 9