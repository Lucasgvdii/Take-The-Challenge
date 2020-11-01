#The magic square constant problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=120

#Imports
import math

#Main function
"""Instead of building the whole square and getting the constant, I tried to find a mathematical relationship that was generalizable for each magic square"""
def get_magic_constant(square_size,starting_num):
    base=1
    for i in range((square_size-1)//2):
        base=base+4*(i+1)
    return square_size*base-(1-starting_num)*square_size       
          
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(get_magic_constant(5,1)) # --> 65
print(get_magic_constant(3,0)) # --> 12
print(get_magic_constant(3,4)) # --> 24
print(get_magic_constant(7,1)) # --> 175
print(get_magic_constant(9,1)) # --> 369
