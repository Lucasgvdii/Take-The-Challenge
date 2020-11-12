#The digits addition path problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=140

#Main function
def digit_addition(num):
    num=str(num)
    result_num=0
    result_path=""
    
    result_num=result_num+int(num[0])
    result_path=result_path+num[0]
    
    for i in range(1,len(num)):
        result_num=result_num+int(num[i])
        result_path=result_path+" + "+num[i]

    return result_path+" = "+str(result_num)

#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(digit_addition(3433))  # --> 3 + 4 + 3 + 3 = 13
print(digit_addition(64323)) # --> 6 + 4 + 3 + 2 + 3 = 18
print(digit_addition(8))     # --> 8 = 8
