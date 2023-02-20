#===============================================================================
#Program Name: Looped Numbers Divisible by 3 and 5
# Your Name: Keegan Bramlet
# Date: Feb. 19, 2023
# Program Purpose: Display numbers from 1-50, indicating which values are divisible by 3 and 5
#===============================================================================
n=51
for i in range(1, n):
    if (i % 3) == 0 and (i % 5) != 0: 
        print("Divisible by 3")
    if (i % 5) == 0 and (i % 3) != 0:
        print("Divisible by 5")
    if (i % 3) == 0 and (i % 5) == 0:
        print("Divisible by Both")
    if (i % 3) != 0 and (i % 5) != 0:
        print(i)
