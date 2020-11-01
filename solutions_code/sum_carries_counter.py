#The sum carries counter problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=124

#Main function
def get_num_sum_carries(num1,num2):
    
    num1_s=str(num1)
    num2_s=str(num2)
    
    len_num1=len(num1_s)
    len_num2=len(num2_s)
    
    min_len=min(len_num1,len_num2)
    
    total_carries=0
    current_carry=0
    
    for i in range(min_len):
        if (int(num1_s[-1-i])+int(num2_s[-1-i])+current_carry)>9:
            current_carry=1
            total_carries=total_carries+1
        else:
            current_carry=0
    for i in range(len_num1-min_len):
        if (int(num1_s[min_len-2-i])+current_carry)>9:
            current_carry=1
            total_carries=total_carries+1
        else:
            current_carry=0
    for i in range(len_num2-min_len):
        if (int(num2_s[min_len-2-i])+current_carry)>9:
            current_carry=1
            total_carries=total_carries+1
        else:
            current_carry=0
    return total_carries

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(get_num_sum_carries(123,456)) # --> 0
print(get_num_sum_carries(555,555)) # --> 3
print(get_num_sum_carries(123,594)) # --> 1
print(get_num_sum_carries(13,594))  # --> 1
print(get_num_sum_carries(555,5))   # --> 1
