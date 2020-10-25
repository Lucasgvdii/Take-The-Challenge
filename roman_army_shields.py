#The roman army shields problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=119

#Imports
import math

#Main function
def get_num_shields(num_soldiers):
    num_shields=0
    while num_soldiers>0:
        side_length=math.floor(math.sqrt(num_soldiers))
        num_shields=num_shields+side_length*side_length+side_length*4
        num_soldiers=num_soldiers-side_length*side_length
    return num_shields        
          
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(get_num_shields(35)) # --> 71
print(get_num_shields(20)) # --> 44
print(get_num_shields(10)) # --> 26
print(get_num_shields(71)) # --> 123
