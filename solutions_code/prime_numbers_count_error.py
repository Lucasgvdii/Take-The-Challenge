#The prime numbers count aproximation problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=107

#Imports
from math import log as ln

#Main function
def error_count_aproximation(number,error_aux_value):
    
    if number<1 or number>99999 or error_aux_value<0 or error_aux_value>5:
        return "Invalid parameters"
    
    max_error=1/pow(10,error_aux_value)
    aproximate_error=count_primes_1_N(number)/number-1/ln(number) 
    
    if max_error<abs(aproximate_error):
        return "Higher"
    if max_error==abs(aproximate_error):
        return "Equal"
    return "Lower"
    
#Auxiliar function
def count_primes_1_N(number):
    primes=[2]
    for num in range(3,number+1):
        is_prime=True
        for prime in primes:
            if num%prime==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return len(primes)+1


        
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(error_count_aproximation(10,3))     # --> Higher
print(error_count_aproximation(750,2))    # --> Higher
print(error_count_aproximation(65535,2))  # --> Lower 
print(error_count_aproximation(65535,3))  # --> Higher     
print(error_count_aproximation(10000,2))  # --> Higher 
print(error_count_aproximation(99999,1))  # --> Lower 
