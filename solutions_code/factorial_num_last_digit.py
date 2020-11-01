#The factorial numbers problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=114

#Imports
import math

#Main function
def factorials_last_digit(num):
    if num<5:
        return str(math.factorial(num))[-1]
    else:
        return "0"
           
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(factorials_last_digit(2))  # --> 2
print(factorials_last_digit(4))  # --> 4
print(factorials_last_digit(8))  # --> 0
print(factorials_last_digit(19)) # --> 0
