#The kaprekar problem. Link to the explanation of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=100&cat=53

#Main function
def kaprekar_cycles(number):
    numeroK=str(number)
    if len(numeroK)!=4:
        return "The number doesn't have 4 digits"
    if numeroK[:2]==numeroK[2:]:
        return 8
    return kaprekar_rutine(number)

#Auxiliar recursive function
def kaprekar_rutine(number):
    if number==6174:
        return 0
    
    str_number=str(number)
    for i in range(4-len(str_number)):
        str_number= "0" + str_number
        
    all_digits=[]
    for digit in str_number:
        all_digits.append(digit)

    all_digits.sort()
    
    num1=int(all_digits[0]+all_digits[1]+all_digits[2]+all_digits[3])  
    num2=int(all_digits[3]+all_digits[2]+all_digits[1]+all_digits[0])
    
    kaprekar_result=max(num1,num2)-min(num1,num2)
    #Uncomment this line if you want to see the whole process
    #print(str(max(num1,num2))+"-"+str(min(num1,num2))+"="+str(kaprekar_result))
    
    return 1 + kaprekar_rutine(kaprekar_result)
    
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(kaprekar_cycles(3524)) #--> 3
print(kaprekar_cycles(1111)) #--> 8
print(kaprekar_cycles(1121)) #--> 5
print(kaprekar_cycles(6174)) #--> 0
print(kaprekar_cycles(1893)) #--> 7
