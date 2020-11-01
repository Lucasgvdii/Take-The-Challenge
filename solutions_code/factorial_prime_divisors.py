#The factorials "prime divisor". Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=126

#Main function
"""A prime number always has a remainder of 0 when dividing the factorial of
   a number higher than itself, as the factorial will be: 1*2*...*prime*...n.
   If the number is lower than the prime, the division won't have a reminder
   of 0, as the divisor is a prime number and cant be fractioned on lower nums."""
def is_reminder_zero(prime,fact):
    if fact>=prime:
        return "YES"
    else:
        return "NO"

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(is_reminder_zero(2,5))      # --> YES
print(is_reminder_zero(7,500000)) # --> YES
print(is_reminder_zero(7,3))      # --> NO
print(is_reminder_zero(5,8))      # --> YES
