for i in range(100):
    if(i == 34):
        break       #Exit the loop
    print(i)  #prints numbers from 0 to 33, and then breaks the loop when i equals 34


for i in range(100):
    if(i == 34):
        continue    #skip the current iteration and continue with the next iteration of the loop
    print(i)        #prints numbers from 0 to 99, but skips printing 34 due to the continue statement


for i in range(645):
    pass               #pass statement is a null operation; it does nothing when executed.
                       #It can be used as a placeholder for future code.

i = 0
while(i < 10):
    print(i)
    i += 1
