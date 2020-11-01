#The kaprekar numbers problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=115

#Main function
def is_kaprekar_num(num):
    num_pow_2=str(num*num)
    for i in range(len(num_pow_2)-1):
        num1=int(num_pow_2[:i+1])
        num2=int(num_pow_2[i+1:])
        if num2==0:
            return "NO"
        if num1+num2==num:
            return "YES"
    return "NO"
          
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(is_kaprekar_num(22222)) # --> YES
print(is_kaprekar_num(75))    # --> NO
print(is_kaprekar_num(99))    # --> YES
print(is_kaprekar_num(100))   # --> NO
print(is_kaprekar_num(504))   # --> NO
