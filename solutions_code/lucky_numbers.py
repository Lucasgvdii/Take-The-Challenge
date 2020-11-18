#The lucky numbers problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=146

#Main function
def lucky_numbers(numbers):

    numbers_list=[]
    for i in range(1,numbers+1):
        numbers_list.append(i)

    jump =2
    pos  =0
    while jump<=len(numbers_list):
        numbers_list.pop(pos)
        pos=pos+jump-1
        if(pos>=len(numbers_list)):
            pos=0
            jump=jump+1
            
    numbers_list.sort()
    numbers_list.reverse()
    
    return str(numbers)+": "+list2str(numbers_list)

def list2str(nlist):
    strn=""
    for i in nlist:
        strn=strn+str(i)+" "
    return strn
                   
#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(lucky_numbers(3))  # --> 3: 2
print(lucky_numbers(10)) # --> 10: 10 6 4
print(lucky_numbers(30)) # --> 30: 30 22 18 12 10
