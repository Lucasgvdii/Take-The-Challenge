#Esoteric and diabolic squares. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=101

#Main function
def kaprekar_cycles(numbers,lateral_size):
    
    if lateral_size==0:
        return "NO"
    
    magic_constant=diag1_addition(numbers,lateral_size)
    if magic_constant!=diag1_addition(numbers,lateral_size):
        return "NO"
    
    for x in range(lateral_size):
        if magic_constant!=row_addition(numbers,x,lateral_size):
            return "NO"
        if magic_constant!=column_addition(numbers,x,lateral_size):
            return "NO"
    return diabolic_or_esoteric(numbers,lateral_size,magic_constant)

#Main auxiliar function
def diabolic_or_esoteric(numbers,lateral_size,magic_constant):
    
    if len(numbers)!=len(list(set(numbers))):
        return "DIABOLIC"
    if max(numbers)!=(lateral_size*lateral_size):
        return "DIABOLIC"
    if min(numbers)!=1:
        return "DIABOLIC"

    magic_constant2=magic_constant*4//lateral_size
    
    if magic_constant2!=corner_addition(numbers,lateral_size):
        return "DIABOLIC"
    if magic_constant2!=middle_addition(numbers,lateral_size):
        return "DIABOLIC"
    if magic_constant2!=middle_line_addition(numbers,lateral_size):
        return "DIABOLIC"
    return "ESOTERIC"

#Basic auxiliar functions
def row_addition(numbers,row,lateral_size):
    result=0
    for i in range(lateral_size):
        result=result+numbers[row*lateral_size+i]
    return result

def column_addition(numbers,column,lateral_size):
    result=0
    for i in range(lateral_size):
        result=result+numbers[i*lateral_size+column]
    return result

def diag1_addition(numbers,lateral_size):
    result=0
    for i in range(lateral_size):
        result=result+numbers[(lateral_size-1-i)*lateral_size+i]
    return result

def diag2_addition(numbers,lateral_size):
    result=0
    for i in range(lateral_size):
        result=result+numbers[i*lateral_size+i]
    return result

def corner_addition(numbers,lateral_size):
    result=numbers[0]+numbers[lateral_size-1]
    result=result+numbers[lateral_size*(lateral_size-1)]+numbers[lateral_size*lateral_size-1]
    return result

def middle_addition(numbers,lateral_size):    
    result=numbers[lateral_size//2*lateral_size+lateral_size//2]
    
    if lateral_size%2==0:
        result=result+numbers[lateral_size//2*lateral_size+lateral_size//2-1]
        print(result)
        result=result+numbers[(lateral_size//2-1)*lateral_size+lateral_size//2]
        print(result)
        result=result+numbers[(lateral_size//2-1)*lateral_size+lateral_size//2-1]
        return result
    return result*4

def middle_line_addition(numbers,lateral_size):    
    result=numbers[lateral_size//2]
    result=result+numbers[lateral_size//2*lateral_size]
    result=result+numbers[lateral_size//2*lateral_size+lateral_size-1]
    result=result+numbers[lateral_size*(lateral_size-1)+lateral_size//2]
    
    if lateral_size%2==0:
        result=result+numbers[lateral_size//2-1]
        result=result+numbers[(lateral_size//2-1)*lateral_size]
        result=result+numbers[(lateral_size//2-1)*lateral_size+lateral_size-1]
        result=result+numbers[lateral_size*(lateral_size-1)+lateral_size//2-1]
        return result/2
    return result        
    
#You can obviously print these inside the function, but i personally like to keep the code "print-free"
print(kaprekar_cycles([4,9,2,3,5,7,8,1,6],3))                      #--> ESOTERIC
print(kaprekar_cycles([1,2,3,4],2))                                #--> NO
print(kaprekar_cycles([16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1],4)) #--> ESOTERIC
print(kaprekar_cycles([28,21,26,23,25,27,24,29,22],3))             #--> DIABOLIC
print(kaprekar_cycles([2,8,1,6,3,5,7,4,9],3))                      #--> NO
print(kaprekar_cycles([],0))                                       #--> NO
