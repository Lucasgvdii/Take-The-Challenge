#The operation error detector problem. Link to the explanation and heading of the problem --> https://www.aceptaelreto.com/problem/statement.php?id=133

#Main function
def operation_error_detector(base, dividend, divisor, quotient, remainder):

    if base>10:
        operation=(reduce(divisor,base)*reduce(quotient,base)+reduce(remainder,base))%(base-1)
        result=reduce(dividend,base)
    else:
        operation=(int(divisor)*int(quotient)+int(remainder))%(base-1)
        result=int(dividend)%(base-1)

    if operation==result:
        return "Possibly correct"
    return "Incorrect"
        
def reduce(number,base):
    
    reduced_value=0
    for i in number:
        val=traduce_from_base(i)
        reduced_value=reduced_value+int(val)
        
    return reduced_value%(base-1)

def traduce_from_base(value):
    
    traduce_table = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","A":"10",
                     "B":"11","C":"12","D":"13","E":"14","F":"15","G":"16","H":"17","I":"18","J":"19",
                     "K":"20","L":"21","M":"22","N":"23","Ñ":"24","O":"25","P":"26","Q":"27","R":"28",
                     "S":"29","T":"30","U":"31","V":"32","W":"33","X":"34","Y":"35","Z":"36"}
    return traduce_table[value]


#You can obviously print these inside the function, but i personally to keep the code "print-free"
print(operation_error_detector(10,"1732","803","2","126")) # --> Possibly correct
print(operation_error_detector(10,"199","13","16","4"))    # --> Incorrect
print(operation_error_detector(16,"AF","12","9","D"))      # --> Possibly correct
print(operation_error_detector(3,"2","1","1","0"))         # --> Incorrect
