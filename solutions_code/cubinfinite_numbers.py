#The cubinfinite numbers problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=139

#Main function
def is_cubinfinite(num):
    num=str(num)
    path=[num]
    result=get_pow3_digit_adittion(num)
    
    while result not in path and result!="1":
        path.append(result)
        result=get_pow3_digit_addition(result)

    string=""
    for i in path:
        string=string+i+" -> "
        
    if result=="1":
        return string+" 1 -> Cubinfinite"
    return string+" "+result+" -> Not cubinfinite"

def get_pow3_digit_addition(num):
    result=0
    for i in num:
        result=result+pow(int(i),3)
    return str(result)

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(is_cubinfinite(1))    # -> 1 ->  1 -> Cubinfinite
print(is_cubinfinite(10))   # -> 10 ->  1 -> Cubinfinite
print(is_cubinfinite(1243)) # -> 1243 -> 100 ->  1 -> Cubinfinite
print(is_cubinfinite(513))  # -> 513 -> 153 ->  153 -> Not cubinfinite
